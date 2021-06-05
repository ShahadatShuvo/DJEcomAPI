from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    created = models.DateField(auto_now_add=True)
