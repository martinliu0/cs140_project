from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from urllib.parse import urlencode
from django.contrib.messages import info, warning, success
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MainForm, FilterForm, ReviewForm
from .models import Recipe
# Create your views here.
def main_view(request):
	print(request.GET)

	if request.method == 'GET':
		search_form = MainForm(request.GET)
		if search_form.is_valid():
			recipes = Recipe.objects.all()
			search_string = search_form.cleaned_data.get('recipe_name', None)
			recipes = recipes.filter(name__icontains=search_string)
			return render(request, 'recipes/index.html', {'recipes': recipes})

	return render(request, 'recipes/main.html', {'search_form': MainForm(initial=search_form.cleaned_data)})


def index_view(request):
	# if request.method == 'GET':
	# 	search_form = MainForm(request.GET)
	# 	if search_form.is_valid():
	# 		recipes = Recipe.objects.all()
	# 		print(recipes)
	# 		search_string = search_form.cleaned_data.get('recipe_name', None)
	# 		recipes = recipes.filter(name__icontains=search_string)
	# 		return render(request, 'recipes/index.html', {'recipes': recipes})
	return render(request, 'recipes/index.html')
