from django.urls import path
from . import views

urlpatterns=[

    path('', views.home, name='home'),

    path('register', views.register, name='register'),
    path('login',views.user_login,name='user_login'),
    path('logout', views.user_logout, name='logout'),
    path('profile/new', views.profile_create, name='profile_create'),
    path('upload/video', views.video_upload, name='video_upload'),
    path('api/videos', views.JsonResponseVideos, name="JsonResponseVideos"),
    path('home', views.home, name="home"),
    path('video/<int:pk>', views.video_detail, name='video_detail'),
    path('profile', views.profile_view, name='profile_view'),

    
    path('special',views.special, name='special'),
    path('video/<int:pk>/like', views.video_like, name="video_like"),
    path('video/<int:pk>/like/delete', views.video_like_delete, name='video_like_delete'),
    path('video/<int:pk>/dislike', views.video_dislike, name='video_dislike'),
    path('video/<int:pk>/dislike/delete', views.video_dislike_delete, name='video_dislike_delete'),
    path('user/<int:pk>/subscribe', views.subscribe, name="subscribe"),
    path('user/<int:pk>/subscription/delete', views.subscription_delete, name='subscription_delete'),
    path('likes', views.view_likes, name='view_likes'),

    


    path('api/likes', views.sendJsonLikes, name='sendJsonLikes'),
    path('api/dislikes', views.sendJsonDislikes, name='sendJsonDislikes'),
    path('api/comments', views.sendJsonComments, name='sendJsonComments'),
    path('api/subscriptions', views.sendJsonSubscriptions, name='sendJsonSubscriptions'),
]

