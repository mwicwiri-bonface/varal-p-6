from django.contrib.auth.forms import UserCreationForm
from .models import Mto


class MtoRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Mto
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_mto = True
        user.is_active = True
        if commit:
            user.save()
        return user
