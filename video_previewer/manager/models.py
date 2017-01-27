import uuid

from django.db import models

from manager.validators import validate_file_extension

# Create your models here.


class Video(models.Model):
    STATUS_CHOICES = (
        (1, 'Готово'),
        (2, 'В очереди'),
        (3, 'На обработке'),
        (4, 'Ошибка обработки')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey('VideoCategory', on_delete=models.CASCADE)
    length = models.TimeField(null=True, blank=True, editable=False)
    preview = models.ImageField(
        width_field=100, height_field=100, null=True,
        blank=True, editable=False, upload_to='img/')
    status = models.IntegerField(choices=STATUS_CHOICES, default=3)
    file = models.FileField(
        upload_to='video/', validators=[validate_file_extension])

    def __str__(self):
        return self.file.name


class VideoCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
