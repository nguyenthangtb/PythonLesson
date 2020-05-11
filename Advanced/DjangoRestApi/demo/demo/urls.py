"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from rest.views import PostListCreateAPIView, PostDetailUpdateAPIView
from rest.views import UserListCreateAPIView, UserDetailUpdateAPIView

# đăng ký API vào router
router = routers.SimpleRouter()
router.register(r'posts', PostListCreateAPIView, basename="Posts")     
router.register(r'posts', PostDetailUpdateAPIView, basename="Posts")


router.register(r'users', UserListCreateAPIView, basename="Users")
router.register(r'users', UserDetailUpdateAPIView, basename="Users")

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/', include(router.urls))  #  Đăng ký router url vào project url
]
