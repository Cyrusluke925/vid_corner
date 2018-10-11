from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from django.utils import timezone
# Create your models here.


class UserProfileInfo(models.Model):
    channel_name = models.CharField(max_length=70)
    about = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, upload_to=settings.MEDIA_ROOT, null=True, default=settings.MEDIA_ROOT+'/defaultprofile.jpg')
    header_picture = models.ImageField(blank=True, upload_to=settings.MEDIA_ROOT, null=True, default=settings.MEDIA_ROOT+'/defaultheader.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username


class Video_Upload(models.Model):
    video = models.ImageField(upload_to=settings.VIDEO_ROOT)
    created_at = models.DateTimeField()
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    def created_at_format(self):
        return self.created_at.strftime('%b %e %Y')
    