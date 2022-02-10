from django.http import HttpResponse
from django.shortcuts import render
from .models import Pet, PetPhoto, Profile


# Create your views here.
def home(request):
    context = {}
    return render(request, 'home_page.html', context)


def dashboard(request):
    photos = PetPhoto.objects.all()
    print(photos)
    context = {
        'photos': photos,
    }
    return render(request, 'dashboard.html', context)


def profile(request):
    profile = Profile.objects.all()[0]
    images = PetPhoto.objects.filter(tagged_pets__user_profile=profile.id)
    total_likes = 0
    for image in images:
        total_likes += image.likes
    number_of_images = len(images)

    profile_images = None
    for image in images:
        if image == profile.id:
            pass
    page = 'profile'
    context = {
        'page': page,
        'profile': profile,
        'number_of_images': number_of_images,
        'total_likes': total_likes,
        'images': images,
    }
    return render(request, 'profile_details.html', context)


def photo_details(request, id):
    context = {}
    return render(request, 'photo_details.html', context)


def error_page(request):
    return HttpResponse('<h1>Error page</h1>')


def create_profile(request):
    return render(request, 'create_profile.html')


def add_photo(request):
    context = {}
    return render(request, 'add_photo.html', context)
