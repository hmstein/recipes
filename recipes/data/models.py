from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    blurb = models.CharField(max_length=200)
    credits = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class Step(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    measurement = models.CharField(max_length=200)
    amount = models.FloatField()
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
