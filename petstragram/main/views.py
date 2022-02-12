from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateProfileForm
from .models import Pet, PetPhoto, Profile


# Create your views here.
from ..common.tools import get_profile


def home(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'home_page.html', context)


def dashboard(request):
    photos = PetPhoto.objects.all()
    print(photos)
    context = {
        'photos': photos,
    }
    return render(request, 'dashboard.html', context)


def profile(request):
    profile = get_profile()
    images = PetPhoto.objects.filter(tagged_pets__user_profile=profile.id)
    total_likes = 0
    for image in images:
        total_likes += image.likes
    number_of_images = len(images)

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
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=id)

    print(pet_photo)
    context = {
        'photo': pet_photo,

    }
    return render(request, 'photo_details.html', context)


def update_likes(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    photo.likes += 1
    photo.save()
    return redirect('photo-details', pk)


def error_page(request):
    return HttpResponse('<h1>Error page</h1>')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profile_create.html', context)


def add_photo(request):
    context = {}
    return render(request, 'add_photo.html', context)
