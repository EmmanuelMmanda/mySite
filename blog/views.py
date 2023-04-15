from django import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Gallery, Tag, Post, Comment


def homepage(request):
    try:
        gallery_items = Gallery.objects.all()
        render_html = render_to_string('blog/index.html', {
            'gallery_items': gallery_items
        })
        return HttpResponse(render_html)
    except Gallery.DoesNotExist:
        raise Http404()


def posts(request):
    try:
        post_data = Post.objects.all()
        render_html = render_to_string('blog/posts.html', {
               "post_data": post_data,
                "recent_posts": post_data,
            })
        return HttpResponse(render_html)
    except Post.DoesNotExist:
        raise Http404()


def post_detail(request, slug):
    try:
        single_post = Post.objects.get(slug=slug)
        recent_posts = Post.objects.all()
        post_comments = single_post.comment.all()
        render_html = render(request, 'blog/blog-single.html', {
            'post': single_post,
            'recent_posts': recent_posts,
            'post_comments': post_comments
        })
        return HttpResponse(render_html)
    except Post.DoesNotExist:
        raise Http404()


def contact(request):
    try:
        render_html = render(request, 'blog/contact.html')
        return HttpResponse(render_html)
    except:
        raise Http404()


def comment(request, slug):
    print(request)
    print(slug)
