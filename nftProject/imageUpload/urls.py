
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from imageUpload import views

app_name = "imageUpload"

urlpatterns = [
    path('fileUpload/', views.fileUpload, name="fileUpload"),
]