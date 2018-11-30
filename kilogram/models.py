from django.db import models
import django_tables2 as tables
from .forms import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# class SimpleTable(tables.Table):
#   class Meta:
#     model = User

# class UserIn(models.Model):
#   name = models.CharField(max_length=20)
#   user_id= models.CharField(max_length=30)
#   user_psw= models.


class Grade(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    grade = models.IntegerField()
#
# class GroupB(models.Model):
#     user_b =models.ForeignKey(User, related_name='grouping_b',on_delete=models.CASCADE)
#     group_b = models.IntegerField()

# class ProfileTable(tables.Table):
#   class Meta:
#     model = GroupA
#
# class Related(tables.Table):
#   class Meta:
#     model = User
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#   if created:
#     Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#   instance.profile.save()