"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from kilogram import views as kilogram_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',kilogram_views.IndexView.as_view(), name="root"),
    path('kilogram/',include('kilogram.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    # path('accounts/logout/',auth_views.logout,{'next_page':'/'}),
    path('login',auth_views.login,{'templates_name':'login.html'}),
    path('accounts/signup',kilogram_views.CreateUserView.as_view(), name='signup'),
    # path('accounts/login/done',kilogram_views.RegisterView.as_view(), name='create_user_done'),
]
