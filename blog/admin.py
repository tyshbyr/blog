from django.contrib import admin

# Register your models here.
from .models import Category, Subcategory, Article

class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Article, ArticleAdmin)