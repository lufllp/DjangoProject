from django import forms
from .models import Item, Category, Album


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'item', 'category', 'author']
