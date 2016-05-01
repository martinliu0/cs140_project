from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import models as auth_models

# Create your models here.

class Recipe(models.Model):
	name = models.CharField(max_length=50, blank=False)

class Unit(models.Model):
	TEASPOON = 'tsp'
	TABLESPOON = 'tbsp'
	CUP = 'c'
	PINT = 'pt'
	GALLON = 'gal'
	LITER = 'L'
	ML = 'cc'

	POUND = 'lb'
	OUNCE = 'oz'
	MG = 'mg'
	G = 'g'
	KG = 'kg'

	INCH = 'in'
	CM = 'cm'
	MM = 'mm'


class Recipe(models.Model):
	name = models.CharField(max_length=50, blank=False)


class Ingredient(models.Model):
	name = models.CharField(max_length=50, blank=False)
	instructions = models.CharField(max_length=300, blank=False)

class RecipeIngredients(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredient = models.ForeignKey(Ingredient)
	unit = models.ForeignKey(Unit)

	quantity = models.DecimalField(max_digits=2, blank = False, decimal_places = 1)

	
	def get_dependencies(self):
		pass



class Review(models.Model):
    stars = models.IntegerField(blank = False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField()
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(auth_models.User)

