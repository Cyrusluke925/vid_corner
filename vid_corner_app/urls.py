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

    # path('api/users', views.sendJson, name='sendJson'),
    path('special',views.special, name='special'),
    path('video/<int:pk>/like', views.video_like, name="video_like"),
    path('video/<int:pk>/like/delete', views.video_like_delete, name='video_like_delete'),
]

