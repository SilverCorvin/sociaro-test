# from django.shortcuts import render
from django.views.generic import ListView, CreateView

from manager.forms import VideoUploadForm
from manager.models import Video

# Create your views here.


class VideoUploadView(CreateView):
    template_name = 'upload.html'
    form_class = VideoUploadForm
    success_url = '/manage/status'


class VideoLibraryView(ListView):
    model = Video
    template_name = 'library.html'
