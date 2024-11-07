from django.db import models
from django.contrib.auth.models import User


class Plane(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='planes/')
    description = models.TextField()
    text = models.TextField()
    date_publications = models.DateTimeField(auto_now_add=True)
    plan = models.ImageField(upload_to='plan/')
    plane_type = models.CharField(max_length=255)
    complexity_level = models.CharField(max_length=255)
    download_link = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Component(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.PositiveIntegerField()  # Количество на складе
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # Тип, например, "сервоприводы", "батарейки"


class SelectedParts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    part = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} selected {self.quantity} of {self.part.name}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cart.user.username} - {self.component}"
