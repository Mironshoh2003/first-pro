from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='mahsulot nomi')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='maxsulot narxi')
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-name',)
        index_together = (('id'),)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='', verbose_name='mahsulot surati', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
