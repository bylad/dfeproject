# Generated by Django 3.1.3 on 2021-05-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210513_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryblog',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, verbose_name='URL-адрес'),
        ),
    ]
