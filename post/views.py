from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from comment.forms import CommentForm
from django.contrib.auth import authenticate

from post.models import Tag, Post, Follow, Stream, Likes
from post.forms import NewPostForm
from userauths.models import Profile
from comment.models import Comment
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        all_users = User.objects.all()
        profile = Profile.objects.all()
        posts = Stream.objects.filter(user=user)
        group_ids = []

        for post in posts:
            group_ids.append(post.post_id)
        
        post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
        context = {
            'post_items':post_items,
            'all_users':all_users,
            'profile':profile
        }
        return render(request, 'index.html', context)
    else:
        return redirect('sign-in')

@login_required
def NewPost(request):
    user = request.user.id
    tags_objs = []

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tag')
            tags_list = list(tag_form.split(','))

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)

            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            p.tag.set(tags_objs)
            p.save()
            return redirect('index')
    
    else:
        form = NewPostForm()
    
    context = {
        'form':form
    }

    return render(request, 'newpost.html', context)

@login_required
def PostDetails(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # comments
    comments = Comment.objects.filter(post=post).order_by('-date')

    # comment form
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            return HttpResponseRedirect(reverse('post-details', args=[post_id]))
    else:
        form = CommentForm

    context = {
        'form':form,
        'comments':comments,
        'post':post
    }

    return render(request, 'post-details.html', context)

@login_required
def tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tag=tag).order_by('-posted')
    context = {
        'posts':posts,
        'tag':tag
    }

    return render(request, 'tags.html', context)


def like(request, post_id, code):
    user = request.user
    post = Post.objects.get(id=post_id)
    curr_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        liked = Likes.objects.create(user=user, post=post)
        curr_likes += 1
    else:
        liked = Likes.objects.filter(user=user, post=post).delete()
        curr_likes -= 1
    
    post.likes = curr_likes
    post.save()
    if code==1:
        return HttpResponseRedirect(reverse('index'))
    elif code==2:
        return HttpResponseRedirect(reverse('post-details', args=[post_id]))

def favourite(request, post_id, code):
    user = request.user
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(user=user)

    if profile.favourite.filter(id=post_id).exists():
        profile.favourite.remove(post)
    else:
        profile.favourite.add(post)

    if code==1:
        return HttpResponseRedirect(reverse('index'))
    elif code==2:
        return HttpResponseRedirect(reverse('post-details', args=[post_id]))