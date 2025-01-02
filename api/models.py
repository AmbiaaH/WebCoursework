from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"

class Hobby(models.Model):
    title = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title
    
class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    hobbies = models.ManyToManyField(Hobby)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.username

class Status(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class FriendRequest(models.Model):
    sender_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests', on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_requests', on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1)