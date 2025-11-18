from django.db import models

class Category_Clothes(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category_Clothes, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)   # связь сортировки

    def __str__(self):
        return self.name
