# Generated by Django 3.2.8 on 2021-10-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_druft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='druft',
        ),
        migrations.AddField(
            model_name='article',
            name='to_publish',
            field=models.BooleanField(default=True, verbose_name='Опубликовать'),
        ),
    ]
