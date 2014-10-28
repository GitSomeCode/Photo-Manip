from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class ProfilePic(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    avatar_tn = ImageSpecField(source='avatar',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60})


