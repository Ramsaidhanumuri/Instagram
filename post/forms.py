from django import forms
from post.models import Post

class NewPostForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Captions'}), required=False)
    tag = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Tags - Separate tag with comma'}), required=False)
    
    class Meta:
        model = Post
        fields = ['picture', 'caption', 'tag']
