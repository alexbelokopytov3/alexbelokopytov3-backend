from django import forms

from .models import Post



class PostView(forms.ModelForm):
    image_posts = forms.ImageField(widget=forms.FileInput, required=False)
    class Meta:
        model = Post
        fields = (
            'category_post',
            'title_post',
            'text_post',
            'image_posts', 
            )