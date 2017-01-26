from django.contrib import admin
from manager.models import Video, VideoCategory

# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    pass
