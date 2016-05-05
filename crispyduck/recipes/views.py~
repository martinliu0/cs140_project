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
    recipes = Recipe.objects.all()
    
    if 'reset' in request.GET:
        if 'sortfilt' in request.session:
            request.session.pop('sortfilt')
        return redirect(reverse('index'))

    settings = request.session.get('sortfilt', {})
    
    search_form = MainForm(request.GET)
    
    # ignore form errors; just get any cleaned data available
    if search_form.is_valid():
        pass

    search_string = search_form.cleaned_data.get('recipe_search', None)
    if search_string:
        recipes = recipes.filter(name__icontains=search_string)
        settings['recipe_search'] = search_string
    elif 'recipe_search' in settings:
        val = settings.get('recipe_search')
        recipes = recipes.filter(name__icontains=val)
        fromsettings = True
        
    return render(request, "recipes/index.html", {'recipes':recipes, 'search_form':MainForm(initial=search_form.cleaned_data)})
	#return render(request, 'recipes/index.html')
	
def details_view(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, "recipes/details.html", {'recipe':recipe})
    
@login_required
def review_view(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            recipe.review_set.create(stars=form.cleaned_data['stars'], review_text=form.cleaned_data['review_text'], user=request.user)
            return redirect('review', id=recipe.id)
    else:
        form = ReviewForm()
    return render(request, "recipes/review.html", {'form':form, 'recipe':recipe})
