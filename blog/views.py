from django.http import request
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.


class CreateMenu():
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()

def create_home_page(request):
    menu = CreateMenu()
    category_list = menu.category
    subcategory_list = menu.subcategory

    return render(request, 'blog/home_page.html', {
        'category_list':category_list,
        'subcategory_list':subcategory_list,
    
    })

def create_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategory_list = Subcategory.objects.filter(category=category.id)
    article_list = Article.objects.all()

    return render(request, 'blog/category_page.html', {
        'subcategory_list':subcategory_list,
        'article_list':article_list,
    })


def create_subcategory_page(request, category_slug, slug):
    subcategory = get_object_or_404(Subcategory, slug=slug)
    article_list = Article.objects.filter(subcategory=subcategory.id)

    return render(request, 'blog/subcategory_page.html', {
        'article_list':article_list,
        'category_slug':category_slug,
        'slug':slug,
    })


def create_article_page(request, category_slug, slug, article_slug):
    article = get_object_or_404(Article, slug=article_slug)

    return render(request, 'blog/article_page.html', {
        'article':article,
        'category_slug':category_slug,
        'slug':slug,
        'article_slug':article_slug,
    })