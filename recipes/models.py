
from django.db import models
import uuid

# Create your models here.

class Category(models.model):
    name = models.CharField(max_length=65),


class Recipe(models.model):
    title = models.CharField(max_length=65),
    description = models.CharField(max_length=150),
    #slug = models.SlugField(),
    id = models.UUIDField(default=uuid.uuid4),
    preparation_time = models.IntegerField(),
    preparation_time_unit = models.CharField(help_text="Quantos Minutos levam para fazer o prato"),
    servings = models.IntegerField(),
    servings_unit = models.CharField(max_length=20),
    preparation_steps = models.TextField(),
    preparation_steps_is_html = models.BooleanField(default=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True),
    is_published = models.BooleanField(default=False),
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/'),

    #My Foreign key#
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)