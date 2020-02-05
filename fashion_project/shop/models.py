from django.db import models
from django.shortcuts import reverse
from django.conf import settings


class Category(models.Model):
    gender_choice = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('gender_choice',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.gender_choice

    def get_absolute_url(self):
        return reverse("shop:category_display", args=[self.slug])

    def get_add_to_cart_url(self):
        return reverse("add_to_cart", args=[self.slug])


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    img_url = models.URLField(max_length=500)
    quantity = models.IntegerField(default=1)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:single-product", kwargs={
            'slug': self.slug
        })


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title} from {self.item.quantity}'

    def get_total(self):
        total = self.quantity * self.item.price
        float_total = float("{0:.2f}".format(total))
        return float_total



class Order(models.Model):
    order_items = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    orderID = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.order_items.all():
            total += order_item.get_total()
        return total







