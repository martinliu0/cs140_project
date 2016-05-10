from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from urllib.parse import urlencode
from django.contrib.messages import info, warning, success, error
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MainForm, ReviewForm
from .models import Recipe

# Create your views here.

def main_view(request):
    print(request.GET)
    if 'recipe_name' in request.session:
        request.session.pop('recipe_name')
    if request.method == 'GET':
        search_form = MainForm(request.GET)
        if search_form.is_valid():
            recipes = Recipe.objects.all()
            search_string = search_form.cleaned_data.get('recipe_name', None)
            recipes = recipes.filter(name__icontains=search_string)
            return render(request, 'recipes/index.html', {'recipes': recipes, 'search_form':MainForm(initial=search_form.cleaned_data), "index_query": 'recipe_name={}'.format(search_string)})
    return render(request, 'recipes/main.html', {'search_form':MainForm(initial=search_form.cleaned_data)})

def index_view(request):
    recipes = Recipe.objects.all()
    
    if not len(request.GET):
        if 'recipe_name' in request.session:
            request.session.pop('recipe_name')
        print ("cleared saved settings")
        return redirect(reverse('main'))

    saved_search = request.session.get('recipe_name', "")
    
    if 'sort' in request.GET:    
        sortorder = request.GET.get('sort', '')
        recipes = recipes.filter(meal__icontains=sortorder)
    
    search_form = MainForm(request.GET)

    if search_form.is_valid():
        pass

    search_string = search_form.cleaned_data.get('recipe_name', None)
    print(search_string, saved_search)
    if search_string:
        recipes = recipes.filter(name__icontains=search_string)
        request.session['recipe_name'] = search_string
    elif len(saved_search):
        recipes = recipes.filter(name__icontains=saved_search)
        search_string=saved_search

    return render(request, 'recipes/index.html', {'recipes': recipes, 'search_form':MainForm(initial=search_form.cleaned_data), "index_query": 'recipe_name={}'.format(search_string)})
	
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
            return redirect('details', id=recipe.id)
    else:
        form = ReviewForm()
    return render(request, "recipes/review.html", {'form':form, 'recipe':recipe})
    
def restaurants_view(request):
    return render(request, "recipes/restaurants.html")
