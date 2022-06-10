# Generated by Django 3.1.3 on 2022-05-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0002_auto_20220331_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industryindex',
            name='cur_year_index',
            field=models.FloatField(verbose_name='current'),
        ),
        migrations.AlterField(
            model_name='industryindex',
            name='pre_cur_index',
            field=models.FloatField(verbose_name='preceed-current'),
        ),
        migrations.AlterField(
            model_name='industryindex',
            name='pre_year_index',
            field=models.FloatField(verbose_name='preceed'),
        ),
        migrations.AlterField(
            model_name='industryproduction',
            name='cur_year_production',
            field=models.FloatField(verbose_name='current'),
        ),
        migrations.AlterField(
            model_name='industryproduction',
            name='pre_cur_production',
            field=models.FloatField(verbose_name='preceed-current'),
        ),
    ]
