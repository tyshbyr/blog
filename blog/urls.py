from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.create_home_page, name='home_page'),
    path('<slug:slug>', views.create_category_page, name='category_page'),
    re_path(r'^(?P<category_slug>[\w-]+)/(?P<subcategory_slug>[\w-]+)/$', views.create_subcategory_page, name='subcategory_page'),
    re_path(r'^(?P<category_slug>[\w-]+)/(?P<subcategory_slug>[\w-]+)/(?P<article_slug>[\w-]+)$', views.create_article_page, name='article_page'),
]
