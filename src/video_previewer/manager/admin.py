from django.contrib import admin
from manager.models import Video, VideoCategory

# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    pass


class VideoCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)
admin.site.register(VideoCategory, VideoCategoryAdmin)
