import os

from django.db import models
from django.core.exceptions import ValidationError


def validate_media_file(file):
    extension = os.path.splitext(file.name)[1].lower()

    allowed_extensions = {
        'image': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
        'video': ['.mp4', '.webm', '.ogg'],
        'audio': ['.mp3', '.wav', '.ogg', '.m4a'],
    }

    media_type = getattr(file, '_media_type', None)

    if extension not in [
        '.jpg', '.jpeg', '.png', '.gif', '.webp',
        '.mp4', '.webm', '.ogg', '.mp3', '.wav', '.m4a'
    ]:
        raise ValidationError('Unsupported multimedia file format.')


class MediaItem(models.Model):

    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='media_files/')
    date_added = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()

        if self.file and self.media_type:
            extension = os.path.splitext(self.file.name)[1].lower()

            allowed_extensions = {
                'image': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
                'video': ['.mp4', '.webm', '.ogg'],
                'audio': ['.mp3', '.wav', '.ogg', '.m4a'],
            }

            if extension not in allowed_extensions[self.media_type]:
                raise ValidationError({
                    'file': f'Invalid file format for {self.media_type}.'
                })

    def __str__(self):
        return self.title