from django.urls import path
from . import views

urlpatterns=[
    

    path('', views.home, name='home'),
    path('home', views.home, name="home"),

# +++++++++++++++++++ LOGIN AND REGISTER AND LOGOUT ++++++++++++++++++++++++++++++
    path('register', views.register, name='register'),
    path('login',views.user_login,name='user_login'),
    path('logout', views.user_logout, name='logout'),



# ++++++++++++++++ VIDEO LINKS +++++++++++++++ VIDEO LINKS ++++++++++++++++++
    path('video/<int:pk>', views.video_detail, name='video_detail'),
    path('video/<int:pk>/like', views.video_like, name="video_like"),
    path('video/<int:pk>/like/delete', views.video_like_delete, name='video_like_delete'),
    path('video/<int:pk>/dislike', views.video_dislike, name='video_dislike'),
    path('video/<int:pk>/dislike/delete', views.video_dislike_delete, name='video_dislike_delete'),
    path('video/<int:pk>', views.video_detail, name='video_detail'),
    path('upload/video', views.video_upload, name='video_upload'),




    # +++++++++++++++++++++++++++ PROFILE, SUBSCRIBE, +++++++++++++++++++++++++++++++
    path('likes', views.view_likes, name='view_likes'),
    path('feed', views.subscribedVideo, name='subscribedVideo'),
        path('user/<int:pk>/subscribe', views.subscribe, name="subscribe"),
    path('user/<int:pk>/subscription/delete', views.subscription_delete, name='subscription_delete'),
    path('profile', views.profile_view, name='profile_view'),
    path('profile/new', views.profile_create, name='profile_create'),
    path('user/<int:pk>/profile', views.other_profile, name="other_profile"),

    
# +++++++++++++++ API LINKS ++++++++++++ API LINKS +++++++ API LINKS ++++++++++++ # 
    path('api/likes', views.sendJsonLikes, name='sendJsonLikes'),
    path('api/dislikes', views.sendJsonDislikes, name='sendJsonDislikes'),
    path('api/comments', views.sendJsonComments, name='sendJsonComments'),
    path('api/subscriptions', views.sendJsonSubscriptions, name='sendJsonSubscriptions'),
    path('api/users', views.sendJsonUsers, name='sendJsonUsers'),
    path('api/videos', views.JsonResponseVideos, name="JsonResponseVideos"),
]

