from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django_request_mapping import request_mapping

from web.models import Category

@request_mapping("/custcen/notice", method="post")
def notice(request, Post=None):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 15)
    categories = Category.objects.all()
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        context = {'posts': posts, 'categories': categories}

    return render(request, 'custcen/notice.html', context)


@request_mapping("/custcen/notice_d", method="get")
def notice_detail(request, pk, Post=None):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {"post": post, "categories": categories}

    return render(request, 'custcen/notice_d.html', context)