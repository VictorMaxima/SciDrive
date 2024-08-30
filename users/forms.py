from django import forms
from django.contrib.auth.forms import UserCreationForm
import logging
logger = logging.getLogger(__name__)
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1',
         'password2')
        field_classes = {"email": UsernameField}

class MyBackend(BaseBackend):
    def authenticate( request, email=None, password=None):
        try:
            user = Individual.objects.get(email=email, password=password)
        except Individual.DoesNotExist:
            print(Individual.objects)
            return None
        print(Individual.objects)
        print("yes")
        return user
    def get_user(self, client_id):
        try:
            return Individual.objects.get(pk=client_id)
        except Individual.DoesNotExist:
            return None

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(strip=False, widget=forms.PasswordInput)
    
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.User = None
        super().__init__(*args, **kwargs)
    
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        print(email)
        print(password)
        if email and password:
            self.User = authenticate(
                self.request, email=email, password=password
            )
            if self.User is None:
                raise forms.ValidationError(
                    "Invalid email/password combination "
                )
            logger.info("Authentication successful for %s", email )
        return self.cleaned_data
    def get_user(self):
        return self.User