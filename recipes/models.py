from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65, help_text='enter your category name')

    def __str__(self):
       return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=150, help_text='A brief description about the recipe')
    slug = models.SlugField(help_text='recipe title with - between de words, ex: the-recipe-title-goes-here')
    preparation_time = models.IntegerField(help_text='in minutes')
    preparation_time_unit = models.CharField(max_length=65, help_text='minutes or hours')
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=20)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')

    # My Foreign key #
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
