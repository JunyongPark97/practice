from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
# Register your models here.
class ProfileInline(admin.StackedInline):
  model = Grade
  can_delete = False
  verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
  inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Grade)
# admin.site.register(GroupB)