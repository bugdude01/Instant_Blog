from django import forms
from .models import Post

"""
Basic layout for  simple blog form
"""

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
