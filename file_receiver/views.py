from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return HttpResponse("Hello, you are ready to handle files!")


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()

        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'file_receiver/upload.html', context=context)