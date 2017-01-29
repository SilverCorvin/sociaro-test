import os

from django.core.management.base import BaseCommand, CommandError
from django.core.files.images import ImageFile
from django.core.files.temp import NamedTemporaryFile
import imageio

from manager.models import Video


def get_normalized_duration(seconds):
    ''' Принимает на вход время в секундах. Возвращает время в формате HH:MM:SS '''
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


class Command(BaseCommand):
    help = 'Команда подсчитывает продолжительность видео и генерирует превью'

    def handle(self, *args, **options):
        self.stdout.write("Задача запущена")
        videos = Video.objects.filter(status=2)
        for video in videos:
            video.status = 3
            video.save()
            try:
                filepath = video.file.path
                videodata = imageio.get_reader(filepath, 'ffmpeg')
                middle_frame = videodata.get_data(len(videodata) // 2)
                tmpfile = NamedTemporaryFile(suffix='.jpeg')
                imageio.imwrite(tmpfile, middle_frame, format='jpeg')
                video.duration = get_normalized_duration(videodata._meta['duration'])
                video.preview = ImageFile(tmpfile, os.path.basename(tmpfile.name))
                video.status = 1
                video.save()
            except:
                video.status = 4
                video.save()
                raise
                #raise CommandError(
                #    "Ошибка {} обработки видео с id: {}".format(e, video.id))
        self.stdout.write("Задача завершена")
