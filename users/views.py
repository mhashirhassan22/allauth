from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        f = request.POST['file']
        oc = owncloud.Client('http://domain.tld/owncloud')
        oc.login('user', 'password')
        oc.mkdir('testdir')
        oc.put_file(f, 'localfile.txt')
        link_info = oc.share_file_with_link(f)
        print(link_info.get_link())
        return render(request, 'home.html', {'msg':"return"})