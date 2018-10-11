from django.shortcuts import render, redirect
from vid_corner_app.forms import UserForm, UserProfileInfoForm, VideoUploadForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Video_Upload
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'vid_corner_app/index.html')


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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else: 
                return HttpResponse('Your account is inactive.')
        else:
            print('Login Failed')
            print(f'they used username: {username} and password: {password}')
            return HttpResponse('Invalid login details given')
    else:
        #We might need to change the path when we create this form
        return render(request, 'vid_corner_app/login.html', {})





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

            return render(request, 'vid_corner_app/profile_view.html')
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
        return redirect('index')
    else: 
        form = VideoUploadForm()
        return render(request,'vid_corner_app/video_upload.html', {'form':form})


def home(request):
    videos = Video_Upload.objects.all().order_by('?')
    paginator = Paginator(videos, 9)
    page = request.GET.get('page')
    thevideos = paginator.get_page(page)
    print('The videos are', videos)
    return render(request, 'vid_corner_app/home.html', {'videos': thevideos})