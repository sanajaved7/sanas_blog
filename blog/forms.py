from django import forms
from .models import Post, Tag


class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    text = forms.CharField(widget=forms.Textarea, label="Blog Text")
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label="Tags",required=False)
    new_tags = forms.CharField(label="New Tag", max_length=100, required=False)

    #class Meta:
        #model = Post
        #fields = ('title', 'text', 'tags')
