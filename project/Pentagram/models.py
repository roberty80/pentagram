from uuid import uuid1
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.
def photos_directory(instance, filename):
    return 'photos/user_{0}/{1}_{2}'.format(instance.user.username, str(uuid1()), filename)


class Photo(models.Model):
    user = models.ForeignKey(User)
    counter_like = models.IntegerField(default=0)
    photo = models.ImageField(upload_to = photos_directory, null = True)


class Comment(models.Model):
    user = models.ForeignKey(User)
    photo_id = models.ForeignKey(Photo)
    comment = models.TextField(null=False)


@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created= False, **kwargs):
    if created:
        Token.objects.create(user=instance)






'''class Post(models.Model):
    """
    [...]
    """
    likes = models.PositiveIntegerField(default=0)

    @property
    def total_likes(self):
        return self.likes.count()'''
