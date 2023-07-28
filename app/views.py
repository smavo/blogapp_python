from django.shortcuts import render
from app.models import Post, Tag, Comments
from app.forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'app/index.html')


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comments.objects.filter(post=post)
    form = CommentForm()

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            postid = request.POST.get('post_id')
            post = Post.objects.get(id=postid)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))

    tags = Tag.objects.all()

    if post.view_count is None:
        post.view_count = 1
    else:
        # post.view_count = post.view_count + 1
        post.view_count += 1
    post.save()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'tags': tags,
    }
    return render(request, 'app/post.html', context)

