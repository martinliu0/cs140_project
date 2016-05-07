from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import models as auth_models

# Create your models here.

class Recipe(models.Model):
	APPETIZER = "AT"
	MAIN = "MN"
	DESSERT = "DS"

	MEAL_CHOICES = ((MAIN, "Main"), (DESSERT, "Dessert"), (APPETIZER, "Appetizer"))

	name = models.CharField(max_length=100, blank=False)
	image = models.ImageField(blank=False, default="http://ba3d96e768581514f6ec-e6b856593874a8f38a8aa2d89e1f03ce.r54.cf2.rackcdn.com/default_food_large.jpg") 
	description = models.CharField(max_length=800, blank=False, default="")
	ingredients = models.CharField(max_length=800, blank=False, default="")
	time = models.IntegerField(default=0, validators=[MaxValueValidator(600), MinValueValidator(0)])
	meal = models.CharField(max_length=2, choices=MEAL_CHOICES, default=MAIN)

	def get_time_str(self):
		time = float(self.time)
		if float(self.time) > 60.0:
			return "{} hr {} min".format(int(time // 60), int(time % 60))
		return "{} min".format(int(time))

	def __str__(self):
		return self.name

	def get_ingredients(self):
		return self.ingredients.split("**")

class RecipeInstruction(models.Model):
	
	recipe = models.ForeignKey(Recipe)
	step = models.IntegerField(default=0, validators=[MaxValueValidator(20), MinValueValidator(1)])
	instruction = models.CharField(max_length=1000, blank=False, default="")

	def __str__(self):
		return "Recipe: {} | Step: {}".format(self.recipe, self.step)


	def get_instruction(self):
		return "{}".format(self.instruction)

class Review(models.Model):
    stars = models.IntegerField(blank = False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField()
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(auth_models.User)
    
    def __str__(self):
        return "({} stars) {} (by {})".format(self.stars, self.review_text, self.user)

