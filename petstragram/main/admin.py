from django.contrib import admin
from .models import Profile, Pet, PetPhoto

# Register your models here.
admin.site.register(Profile)
admin.site.register(Pet)
admin.site.register(PetPhoto)