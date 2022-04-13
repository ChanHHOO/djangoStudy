"""mutsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:post_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:post_id>/edit/', views.edit, name="edit"),
    path('<int:post_id>/update/', views.update, name="update"),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/like', views.like, name="like"),
]