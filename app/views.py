from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category, Album, Publisher, Author
from .forms import ItemForm, CategoryForm, AlbumForm, PublisherForm, AuthorForm


def item_list(request):
    albums = Album.objects.select_related('item', 'category', 'author__publisher')
    return render(request, 'app/item_list.html', {'albums': albums})


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'app/item_form.html', {'form': form})


def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/item_form.html', {'form': form})


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'item': item})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/item_list.html', {'categories': categories})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'app/item_form.html', {'form': form})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'app/item_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'app/item_confirm_delete.html', {'category': category})


def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            item = Item.objects.create(
                name=form.cleaned_data['item_name'],
                description=form.cleaned_data['item_description']
            )
            album = form.save(commit=False)
            album.item = item
            album.cover_url = form.cleaned_data['cover_url']  # <- ESSENCIAL
            album.save()
            return redirect('item_list')
    else:
        form = AlbumForm()
    return render(request, 'app/item_form.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'item': album})


def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = PublisherForm()
    return render(request, 'app/item_form.html', {'form': form})


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = AuthorForm()
    return render(request, 'app/item_form.html', {'form': form})
