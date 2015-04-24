from django import forms
from .models import Post, Tag


class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    text = forms.CharField(widget=forms.Textarea, label="Blog Text")
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label="Existing Tags", required=False)
    # post_tags = forms.ModelMultipleChoiceField(queryset=
    new_tags = forms.CharField(label="New Tag", max_length=100, required=False)
