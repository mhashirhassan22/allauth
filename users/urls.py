from django.urls import path, include, re_path
from .views import *

app_name = 'users'


urlpatterns = [
    path('', index, name="index"),
    path('upload/', file_upload, name="file-upload"),
    path('list/', list_files, name="file-list"),

]