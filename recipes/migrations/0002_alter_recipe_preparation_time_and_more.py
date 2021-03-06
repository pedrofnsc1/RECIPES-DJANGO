# Generated by Django 4.0.4 on 2022-05-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.IntegerField(help_text='in minutes'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time_unit',
            field=models.CharField(help_text='minutes or hours', max_length=65),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(help_text='recipe title with - between de words, ex: the-recipe-title-goes-here'),
        ),
    ]
