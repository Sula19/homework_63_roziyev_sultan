# Generated by Django 4.1.7 on 2023-03-24 11:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0009_alter_post_laked_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments_count',
        ),
        migrations.AddField(
            model_name='post',
            name='commented_post',
            field=models.ManyToManyField(related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='Прокамментированные посты'),
        ),
    ]
