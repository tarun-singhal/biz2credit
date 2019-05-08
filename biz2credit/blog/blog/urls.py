"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
from django.urls import path
from . import views


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

urlpatterns = [
    path('home/', views.home, name='home'),
    path('blog/', views.create_blog, name='create_blog'),
    path('blog-list/', views.blog_list, name='blog_list'),
    path('blog-vote/<id>', views.blog_vote, name='blog_vote')
]
