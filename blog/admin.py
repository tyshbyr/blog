from django.contrib import admin

# Register your models here.
from .models import Category, Subcategory, Article

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Article, ArticleAdmin)