from django.db import models

# Create your models here.
class Recipe(models.Model):
    picture = models.ImageField(upload_to='recipes_image')
    name = models.CharField(max_length=400)
    category = models.CharField(max_length=150)
    description = models.TextField()
    process = models.TextField()
    ingredients = models.TextField()

    def __str__(self):
        return self.name