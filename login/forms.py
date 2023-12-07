from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # User 모델을 import
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()  # 추가적인 사용자 프로필 필드가 있으면 여기에 추가하세요.
        
        from django import forms

