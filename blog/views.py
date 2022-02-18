from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.urls import reverse
from datetime import date

import blog


all_posts = [
    {
        "slug": "hike-in-the-montains",
        "image": "mountains.jpg",
        "author": "Jocc",
        "date": date(2022, 2, 18),
        "title": "Mounten Hiking",
        "excerpt": "There's nothing like the mountains...",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque laborum dolores aperiam cum culpa quas quam dicta voluptas repellendus deserunt accusamus, magni sit distinctio inventore officia! Odit amet consectetur ut?"""
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Jocc",
        "date": date(2022, 2, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Jocc",
        "date": date(2022, 2, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post["date"]


# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    try:
        identified_post = next(
            post for post in all_posts if post["slug"] == slug)
        return render(request, "blog/post-detail.html", {
            "post": identified_post
        })
    except:
        raise Http404()
