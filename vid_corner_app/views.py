from django.shortcuts import render, redirect
from vid_corner_app.forms import UserForm, UserProfileInfoForm, VideoUploadForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Video_Upload, Comment, VideoLike, VideoDislike
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def index(request):
    return render(request, 'vid_corner_app/index.html')


def sendJsonLikes(request):
    likes = list(VideoLike.objects.all().values('video', 'user'))
    return JsonResponse({'likes': likes})


def sendJsonDislikes(request):
    dislikes = list(VideoDislike.objects.all().values('video', 'user'))
    return JsonResponse({'dislikes': dislikes})

    
def JsonResponseVideos(request):
    videos = list(Video_Upload.objects.all().values('user', 'video', 'title', 'description', 'created_at'))
    return JsonResponse({'videos': videos})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form= UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user)
            return redirect('profile_create')
        else: 
            print(user_form.errors)
    else: 
        user_form = UserForm()
    return render(request, 'vid_corner_app/registration.html', {'user_form': user_form, 'registered': registered})



def user_login(request):
    print('hellooooo')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else: 
                return HttpResponse('Your account is inactive.')
        else:
            print('Login Failed')
            print(f'they used username: {username} and password: {password}')
            return HttpResponse('Invalid login details given')
    else:
        #We might need to change the path when we create this form
        return render(request, 'vid_corner_app/home.html', {})




@login_required
def profile_create(request):
    #add registered false and true
    if request.method == "POST":
        print('method is a post ')
        
        form = UserProfileInfoForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            #make a redirect to 
            
            print(request.POST)
            print(request.FILES)

            return render(request, 'vid_corner_app/home.html')
        else: 
            print(form.errors)
            return render(request, 'vid_corner_app/profile_create.html', {'form': form})

    print('about to render')
    form = UserProfileInfoForm()

    return render(request, 'vid_corner_app/profile_create.html', {'form': form})



@login_required
def video_upload(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        print(request.FILES)
        print(form.errors)

        try:
            title = request.POST['title']
            video = request.FILES['video']
            description = request.POST['description']
        except KeyError as e:
            return HttpResponse('Form invalid, missing key {}'.format(e))


        created_at = timezone.datetime.now()
        video = request.FILES['video']
            
        video_upload = Video_Upload(title=title, video=video,description=description, created_at=created_at, user=request.user)
        video_upload.save()
        return redirect('home')
    else: 
        form = VideoUploadForm()
        return render(request,'vid_corner_app/video_upload.html', {'form':form})


def home(request):
    videos = Video_Upload.objects.all().order_by('?')
    paginator = Paginator(videos, 9)
    page = request.GET.get('page')
    thevideos = paginator.get_page(page)
    
    return render(request, 'vid_corner_app/home.html', {'videos': thevideos})


def video_detail(request, pk):
    video = Video_Upload.objects.get(id=pk)
    if request.method == 'POST':
    
        form = CommentForm(request.POST)
        created_at = timezone.datetime.now()
        if form.is_valid():
            content = form.cleaned_data.get('content')
            
            comment = Comment(content=content, created_at=created_at, user=request.user, video=video)
            comment.save()
    
    videos = Video_Upload.objects.all()[:5]
    return render(request, 'vid_corner_app/video_detail.html', {'video': video, 'videos':videos})


@csrf_exempt
def video_like(request, pk):
    print('enters like function')
    if VideoLike.objects.filter(video=pk, user=request.user.id).exists():
        print('You are in the like function and LIKE already Exists')
        likes = []
        return JsonResponse({'likes': likes})

    elif VideoDislike.objects.filter(video=pk, user=request.user.id).exists():
            print('You are in the like function and DISLIKE Already Exists')
            dislikes = []
            return JsonResponse({'dislikes': dislikes})
    else:
        if request.method == "POST":
            print("USER: ", request.user.id)
            
            like = VideoLike(video_id=pk, user=request.user)
            print(like)
            like.save()
            likes = list(VideoLike.objects.filter(video=pk).values('video', 'user'))


            return JsonResponse({'likes': likes})


@csrf_exempt
def video_dislike(request, pk):
    print('enters dislike function')
    if VideoLike.objects.filter(video=pk, user=request.user.id).exists():
        print('You are in the dislike function and LIKE Already Exists')
        likes = []
        return JsonResponse({'likes': likes})

    elif VideoDislike.objects.filter(video=pk, user=request.user.id).exists():
            print('You are in the Dislike function and DISLIKE Already Exists')
            dislikes = []
            return JsonResponse({'dislikes': dislikes})
    else:
        if request.method == "POST":
            print("USER: ", request.user.id)
            
            dislike = VideoDislike(video_id=pk, user=request.user)

            print('disliking noww')
            dislike.save()

            dislikes = list(VideoDislike.objects.filter(video=pk).values('video', 'user'))
            print(dislikes)
            return JsonResponse({'dislikes': dislikes})


@csrf_exempt
def video_like_delete(request, pk):
    print('so you are deleting your like now')
    if request.method == "DELETE":
        video_like = VideoLike.objects.filter(video=pk, user=request.user.id)
        video_like.delete()
    return HttpResponse('like deleted')

@csrf_exempt
def video_dislike_delete(request, pk):
    print('you entered the delete dislike function')
    if request.method == 'DELETE':
        video_dislike = VideoDislike.objects.filter(video=pk, user=request.user.id)
        video_dislike.delete()
    return HttpResponse('dislike object deleted')


        