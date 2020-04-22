from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from .models import File

# Create your views here.
def index(request):
    return HttpResponse("Hello, you are ready to handle files!")


def delete_file(request, pk):
    if request.method == 'POST':
        target_file = File.objects.get(pk=pk)
        target_file.delete()

    return redirect('file_receiver:file_list')


class UploadView(View):
    def get(self, request):
        return render(request, 'file_receiver/upload.html')

    def post(self, request):
        cxt = {}
        try:
            uploaded_file = request.FILES['file']
            file_obj = File(file_name=uploaded_file.name, file_data=uploaded_file)
            file_obj.save()

            return redirect('file_receiver:file_list')
        except:
            cxt['exception'] = 'Failed to upload'
            return render(request, 'file_receiver/upload.html', context=cxt)


class FileListView(View):
    def get(self, request):
        files = File.objects.all()
        return render(request, 'file_receiver/file_list.html', context={
            'files': files
            })
