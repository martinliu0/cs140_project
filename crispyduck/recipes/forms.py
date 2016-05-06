from django import forms 
from .models import Review

class MainForm(forms.Form):
    recipe_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Search recipes...'}))
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'review_text']

