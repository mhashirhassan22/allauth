from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib.auth.admin import UserAdmin
from django.contrib import auth
from .models import *

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):

    list_display = ["username", "is_superuser", 'phone', 'address', 'email']


class FileAdmin(admin.ModelAdmin):
    list_display = ('user','file_path', 'created_at','file_id')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(FileUpload, FileAdmin)



class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'img',)
    list_editable = ('img',)

admin.site.register(BannerImage, BannerImageAdmin)

