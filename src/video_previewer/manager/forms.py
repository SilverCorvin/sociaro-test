from django.forms import ModelForm
from manager.models import Video


class VideoUploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ['category', 'file']
