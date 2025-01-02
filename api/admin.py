from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Hobby, Status, FriendRequest

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Hobby)
admin.site.register(Status)
admin.site.register(FriendRequest)