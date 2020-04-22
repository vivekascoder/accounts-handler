from django.contrib.auth.forms import UserCreationForm, User
from django.forms import Form


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
