from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
import owncloud
from django.core.files.storage import FileSystemStorage
from django.conf import *
from .models import *


def index(request):
    cred = OwnCloudCredential.objects.all().first()
    username, password = cred.username, cred.password
    if not username or not password:
        username = "admin"
        password = "teroarrund90"
    try:
        oc = owncloud.Client('https://lblostenze791.owncloud.online/')
        oc.login(username, password)
        banner = BannerImage.objects.all()
        return render(request, 'index.html',{'banner':banner})
    except:
        return render(request, 'err.html', {'cred':cred})


@login_required
def file_upload(request):
    if request.method == "GET":
        form = DocumentForm()
        return render(request, 'file_upload.html',{'form':form})
    else:
        backup_file = request.FILES['docfile']
        with open('temp/'+str(backup_file), 'wb+') as destination:
            for chunk in backup_file.chunks():
                destination.write(chunk)
        temp_path = os.path.join(settings.BASE_DIR, "temp/" + str(backup_file))
        oc.put_file('testdir/', str(os.path.join(settings.BASE_DIR, "temp/" + str(backup_file))))
        link_info = oc.share_file_with_link('testdir/'+str(backup_file),perms=31)
        os.remove(temp_path)
        try:
            obj = FileUpload()
            obj.user = request.user
            obj.file_path = link_info.get_link()
            obj.file_id = link_info.get_id()
            obj.save()
        except:
            print("Error while creating object in database")
        
        return redirect('users:file-list')

@login_required
def list_files(request):
    files = FileUpload.objects.filter(user=request.user)
    return render(request, 'list.html', {'list':files})
