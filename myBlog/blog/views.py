from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post


def home(request):
    # получаем все записи из Post и делим по 4 штуки на страницу (пагинация)
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # ключи и значения, которые будут выводиться в шаблон
    context = {
        "posts": posts,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, "partial/home.html", context)


def single(request, id=None):
    post = get_object_or_404(Post, id=id)

    context = {
        "post": post,
    }
    return render(request, "partial/single.html", context)
