from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeInstruction
admin.site.register(Recipe)
admin.site.register(RecipeInstruction)

