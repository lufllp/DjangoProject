from django import forms
from .models import Item, Category, Album, Publisher, Author


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    item_name = forms.CharField(label='Nome do Álbum')
    item_description = forms.CharField(
        label='Descrição',
        widget=forms.Textarea,
        required=False
    )
    cover_url = forms.CharField(
        label='URL da Capa',
        required=False
    )

    class Meta:
        model = Album
        fields = ['name', 'category', 'author']  # Removido 'cover_url' daqui


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'country', 'birth_date', 'publisher']
