from django import forms 
from .models import Review

class IngredientForm(forms.Form):
    ingredient_search = forms.CharField(max_length=50, required=True)
    
class FilterForm(forms.Form):
    ingredient_search = forms.CharField(max_length=50, required=True)
    num_ingredients = forms.IntegerField(label="Num of Ingredients", min_value=2, required=True)
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'review_text']
