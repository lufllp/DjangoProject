from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        db_table = 'categoria'


class Publisher(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='publishers')

    class Meta:
        db_table = 'editora'


class Author(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='authors')
    photo_url = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    birth_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'autor'


class Album(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='albums')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'album'
