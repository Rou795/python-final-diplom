from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название магазина')
    url = models.URLField(verbose_name='Ссылка', null=False, blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    shops = models.ManyToManyField(Shop, verbose_name='Магазины')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая розничная цена')

    def __str__(self):
        return f'{self.product.name}, {self.shop.name}'


class Parameter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название параметра')

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, verbose_name='Информация о продукте')
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, verbose_name='Параметр')
    value = models.CharField(max_length=100, verbose_name='Значение')

    def __str__(self):
        return f'{self.product_info}, {self.parameter}, {self.value}'


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    bd_date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    status = models.BooleanField(verbose_name='Статус', null=False, blank=False)

    def __str__(self):
        return f'{self.user}, {self.bd_date}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.order}, {self.product}, {self.shop}, {self.quantity}'


class Contact(models.Model):
    type = models.CharField(max_length=100, verbose_name='Тип')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    value = models.CharField(max_length=100, verbose_name='Значение')

    def __str__(self):
        return f'{self.type}, {self.user}, {self.value}'