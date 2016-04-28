from django.db import models

# Create your models here.
class Recipe(models.Model):
	name = models.CharField(max_length=50, blank=False)



class Ingredient(models.Model):
	name = models.CharField(max_length=50, blank=False)

	instructions = #TBD

class RecipeIngredients(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredient = models.ForeignKey(Ingredient)
	quantity = models.ForeignKey(Unit)


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
	MM = 'MM'

	