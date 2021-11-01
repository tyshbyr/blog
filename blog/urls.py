from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.create_home_page, name='home_page'),
    path('<slug:slug>', views.create_category_page, name='category_page'),
    re_path(r'^(?P<category_slug>.+)/(?P<slug>.+)/$', views.create_subcategory_page, name='subcategory_page'),
]
