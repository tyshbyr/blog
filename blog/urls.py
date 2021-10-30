from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleListView.as_view()),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
