from django.shortcuts import render
from .models import MediaItem


def home(request):
    media_items = MediaItem.objects.all().order_by('-date_added')

    return render(request, 'gallery/home.html', {
        'media_items': media_items
    })


def images(request):
    media_items = MediaItem.objects.filter(media_type='image')

    return render(request, 'gallery/images.html', {
        'media_items': media_items
    })


def videos(request):
    media_items = MediaItem.objects.filter(media_type='video')

    return render(request, 'gallery/videos.html', {
        'media_items': media_items
    })


def audio(request):
    media_items = MediaItem.objects.filter(media_type='audio')

    return render(request, 'gallery/audio.html', {
        'media_items': media_items
    })