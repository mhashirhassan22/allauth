from django.db import models
from django.contrib.auth import get_user_model
# User = get_user_model()
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # key = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    
    def __str__(self):
        return self.username


# Create your models here.
class FileUpload(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='uploader'
    )
    file_path = models.TextField()
    file_id = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)


class BannerImage(models.Model):
    img = models.ImageField()


class OwnCloudCredential(models.Model):
    client_link = models.CharField(max_length=2000, default='https://lblostenze791.owncloud.online/')
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=100)

try:
    if OwnCloudCredential.objects.all().count() < 1:
        obj = OwnCloudCredential.objects.create(username="admin", password="teroarrund90")
except:
    pass
