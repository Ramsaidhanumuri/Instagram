from userauths.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'First Name'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Last Name'}),required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Location'}),required=True)
    # url = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'URL'}),required=True)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Bio'}),required=True)

    class Meta:
        model = Profile
        fields = ['picture', 'first_name', 'last_name', 'location', 'bio']

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'prompt srch_explore'}), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'prompt srch_explore'}), required=False)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Password', 'class':'prompt srch_explore'}), required=False)
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Confirm Password', 'class':'prompt srch_explore'}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']