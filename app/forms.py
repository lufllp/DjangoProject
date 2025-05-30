from django import forms
from .models import Item, Category


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'