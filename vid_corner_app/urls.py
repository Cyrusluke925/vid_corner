from django.urls import path
from . import views

urlpatterns=[

    path('', views.index, name='index'),

    path('register', views.register, name='register'),
    path('user_login',views.user_login,name='user_login'),
    path('logout', views.user_logout, name='logout'),
    path('profile/new', views.profile_create, name='profile_create'),
    path('upload/video', views.video_upload, name='video_upload'),
    path('api/videos', views.JsonResponseVideos, name="JsonResponseVideos"),
    # path('home', views.home, name="home"),

    # path('api/users', views.sendJson, name='sendJson'),
    path('special',views.special, name='special'),
]