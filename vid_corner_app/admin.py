from django.contrib import admin
from . import models

admin.site.register(models.Video_Upload)
admin.site.register(models.Comment)
admin.site.register(models.UserProfileInfo)
admin.site.register(models.VideoLike)
admin.site.register(models.VideoDislike)
# Register your models here.
