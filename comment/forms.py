from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter Comment'}), required=True)

    class Meta:
        model = Comment
        fields = ['body']