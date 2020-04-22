from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import File

# Create your views here.
def index(request):
    return HttpResponse("Hello, you are ready to handle files!")


def upload(request):
    cxt = {}
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['file']
            file_obj = File(file_name=uploaded_file.name, file_data=uploaded_file)
            file_obj.save()

            return redirect('file_receiver:file_list')
        except:
            cxt['exception'] = 'Failed to upload'
            return render(request, 'file_receiver/upload.html', context=cxt)
    else:
        return render(request, 'file_receiver/upload.html')


def file_list(request):
    files = File.objects.all()
    return render(request, 'file_receiver/file_list.html', context={
        'files': files
    })