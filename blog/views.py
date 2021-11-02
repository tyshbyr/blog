from django.http import request
from .models import *
from django.shortcuts import render, get_object_or_404

# Create your views here.


categories_in_menu = Category.objects.all()
subcategories_in_menu = Subcategory.objects.all()



def create_home_page(request):

    return render(request, 'blog/home_page.html', {
        'categories_in_menu':categories_in_menu,
        'subcategories_in_menu':subcategories_in_menu,
    
    })

def create_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategory_list = Subcategory.objects.filter(category=category.id)
    article_list = Article.objects.all()

    return render(request, 'blog/category_page.html', {
        'categories_in_menu':categories_in_menu,
        'subcategories_in_menu':subcategories_in_menu,
        'subcategory_list':subcategory_list,
        'article_list':article_list,
    })


def create_subcategory_page(request, category_slug, slug):
    subcategory = get_object_or_404(Subcategory, slug=slug)
    article_list = Article.objects.filter(subcategory=subcategory.id)

    return render(request, 'blog/subcategory_page.html', {
        'categories_in_menu':categories_in_menu,
        'subcategories_in_menu':subcategories_in_menu,
        'article_list':article_list,
        'category_slug':category_slug,
        'slug':slug,
    })


def create_article_page(request, category_slug, slug, article_slug):
    article = get_object_or_404(Article, slug=article_slug)

    return render(request, 'blog/article_page.html', {
        'categories_in_menu':categories_in_menu,
        'subcategories_in_menu':subcategories_in_menu,
        'article':article,
        'category_slug':category_slug,
        'slug':slug,
        'article_slug':article_slug,
    })