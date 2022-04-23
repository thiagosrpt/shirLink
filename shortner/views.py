from django.shortcuts import render, redirect
import uuid
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        client_uid = request.POST['UID']
        server_uid = str(uuid.uuid4())[:5]
        new_server_url = Url(url=url, uuid=server_uid)
        new_client_url = Url(url=url, uuid=client_uid)
        new_server_url.save()
        new_client_url.save()
        return HttpResponse(server_uid)

def go(request, uuid):
    url_details = Url.objects.get(uuid=uuid)
    return redirect(url_details.url)