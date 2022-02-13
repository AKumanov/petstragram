from django import forms

from petstragram.common.tools import BootstrapFormMixin
from petstragram.main.models import Profile


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'

                }
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }


class UpdateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter description'
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []
