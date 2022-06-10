# Generated by Django 3.1.3 on 2022-06-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docspost',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='docs/images/', verbose_name='Рисунок'),
        ),
        migrations.AlterModelTable(
            name='docscategory',
            table='docs_category',
        ),
        migrations.AlterModelTable(
            name='docspost',
            table='docs_post',
        ),
    ]