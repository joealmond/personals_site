from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.urls import reverse

import blog


blog_posts = {
    "first": "My first blogpost...",
    "second": "My second blogpost...",
    "third": "My third blogpost..."
}


# Create your views here.

def index(request):
    post_list = list(blog_posts.keys())
    last_two_post = post_list[-2:]
    last_two_post.reverse()
    return render(request, "blog/index.html", {
        "last_two_post": last_two_post
    })


def posts(request):
    post_list = list(blog_posts.keys())
    post_list.reverse()
    return render(request, "blog/posts.html", {
        "post_list": post_list
    })


def blog_post_by_number(request, post):
    post_list = list(blog_posts.keys())

    if post > len(post_list):
        return HttpResponseNotFound("Invalid post.")

    redirect_post = post_list[post - 1]
    redirect_path = reverse(
        "post_page", args=[redirect_post])
    return HttpResponseRedirect(redirect_path)


def blog_post(request, post):
    post_text = blog_posts[post]
    return render(request, "blog/post.html", {
        "title": post,
        "post": post,
        "text": post_text
    })
