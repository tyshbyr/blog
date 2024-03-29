# Generated by Django 3.2.8 on 2021-10-30 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Название')),
                ('slug', models.SlugField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Название')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='blog/', verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Текст')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Подкатегория')),
            ],
        ),
    ]
