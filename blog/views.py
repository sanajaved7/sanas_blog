from django.shortcuts import render
from django.utils import timezone
from .models import Post, Tag
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def clean_new_tags(new_tags):
    ''' This function takes the tags that are written and
    adds them to the list of existing list of tags '''
    new_tags = new_tags.split(",")

    new_tag_list = []

    for word in new_tags:
        tag, created = Tag.objects.get_or_create(word=word.strip())
        tag.save()
        new_tag_list.append(tag)
    return new_tag_list

def process_post(cleaned_form, request):
    ''' This function passes in the cleaned form data and creates a post '''
    post = Post(title=cleaned_form["title"], text=cleaned_form["text"])
    post.author = request.user
    post.save()
    tag_list = clean_new_tags(cleaned_form['new_tags'])
    tag_list.extend(cleaned_form['tag'])
    post.tags = tag_list
    return post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = process_post(form.cleaned_data, request)
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_add.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = process_post(form.cleaned_data, request)
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(initial=post.__dict__)
    return render(request, 'blog/post_edit.html', {'form': form})
