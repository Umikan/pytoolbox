from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.files.storage import FileSystemStorage
from . import models
import tempfile
import os


def transcriber(request):
    return render(request, 'transcribe.html', {
                  'server': request.build_absolute_uri('/')})


def transcribe_clip(request):
    with tempfile.TemporaryDirectory() as dname:
        file = request.FILES.get('data')
        FileSystemStorage(location=dname).save(file.name, file)
        filepath = os.path.join(dname, file.name)
        return JsonResponse({'result': models.transcribe(filepath)})
