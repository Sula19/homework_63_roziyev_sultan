# Generated by Django 4.1.7 on 2023-03-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_account_commented_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user_pic', verbose_name='Аватар'),
        ),
    ]
