from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(to_publish=True)
    

class ArticleDetailView(DetailView):
    model = Article
    slug_field = 'slug'





