from django.db import models

# Create your models here.
from datetime import datetime

from django.core.validators import MinLengthValidator
from django.db import models
from .validators import only_letters_validator


# Create your models here.
class Profile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    NO_SHOW = 'Do not Show'
    GENDER_CHOICES = [
        (MALE, ' Male'),
        (FEMALE, 'Female'),
        (NO_SHOW, 'Do not show')
    ]

    first_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters_validator
        ]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters_validator
        ]
    )
    profile_picture = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=11,
        choices=GENDER_CHOICES,
        null=True,
        blank=True
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    Cat = 'Cat'
    Dog = 'Dog'
    Bunny = 'Bunny'
    Parrot = 'Parrot'
    Fish = 'Fish'
    Other = 'Other'
    PET_CHOICES = (
        (Cat, 'Cat'),
        (Dog, 'Dog'),
        (Bunny, 'Bunny'),
        (Parrot, 'Parrot'),
        (Fish, 'Fish'),
        (Other, 'Other'),
    )
    pet_name = models.CharField(
        max_length=30,
        # unique=True,

    )
    pet_type = models.CharField(
        max_length=7,
        choices=PET_CHOICES
    )
    pet_date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.now().year - self.pet_date_of_birth.year

    def __str__(self):
        return f'{self.pet_name}'


class PetPhoto(models.Model):
    photo = models.ImageField(
        null=True,
        blank=True,
        validators=[
            # validate_file_max_size_in_mb(1)
        ]

    )
    tagged_pets = models.ManyToManyField(
        Pet,

        # validate at least 1 pet
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    publication_date_time = models.DateTimeField(
        null=True,
        blank=True,
        auto_created=True
    )

    likes = models.IntegerField(
        default=0
    )
