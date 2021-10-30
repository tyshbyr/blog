from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=35)
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    title = models.CharField(verbose_name='Название', max_length=35)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=130)
    image = models.ImageField(verbose_name='Изображение', upload_to='blog/')
    text = models.TextField(verbose_name='Текст')
    date = models.DateField(auto_now=False)
    subcategory = models.ForeignKey(Subcategory, verbose_name='Подкатегория', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    to_publish = models.BooleanField(verbose_name='Опубликовать', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'