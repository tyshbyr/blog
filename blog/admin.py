from django.contrib import admin

# Register your models here.
from .models import Category, Subcategory, Article

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Article, ArticleAdmin)