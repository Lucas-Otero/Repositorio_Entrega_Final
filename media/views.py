from django.shortcuts import render
from .models import Image

def image_gallery(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'media/image_gallery.html', context)
