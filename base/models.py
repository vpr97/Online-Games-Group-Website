from django.db import models
from django.contrib.auth.models import AbstractUser #using built-in user model from django

class User(AbstractUser):# creating our own user model
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null = True) 
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg") #ImageField relys on the third prty package called pillow- which is a image processing library
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

#creating tables in db for my project
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(User,related_name='participants')# model relationship is many to many
    #as user is already used fot host we cannot use it again. to use it we have to mention related_name
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']


    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[0:50]