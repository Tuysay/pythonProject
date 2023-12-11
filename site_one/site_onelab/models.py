from django.db import models
from django.contrib.auth.models import User
from prompt_toolkit.validation import ValidationError


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, verbose_name='Имя', null=False, blank=True)
    email = models.CharField(max_length=250, verbose_name='Почта', unique=False, null=False, blank=False)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def __str__(self):
        return self.username


class Request(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок заявки', null=False, blank=False)
    description = models.TextField(verbose_name='Описание заявки')
    username = models.ForeignKey(User, verbose_name="Никнейм", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время поста')

    def __str__(self):
        return self.title
