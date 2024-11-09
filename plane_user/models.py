from django.db import models
from django.contrib.auth.models import User


# Модель для хранения информации о самолётах
class Plane(models.Model):
    name = models.CharField(max_length=255)  # Название самолёта
    photo = models.ImageField(upload_to='planes/')  # Фотография самолёта, сохраняется в директории 'planes/'
    description = models.TextField()  # Описание самолёта
    text = models.TextField()  # Дополнительная информация или текстовое описание самолёта
    date_publications = models.DateTimeField(auto_now_add=True)  # Дата публикации, автоматически задаётся при создании
    plan = models.ImageField(upload_to='plan/')  # Изображение чертежа самолёта, сохраняется в директории 'plan/'
    plane_type = models.CharField(max_length=255)  # Тип самолёта
    complexity_level = models.CharField(max_length=255)  # Уровень сложности сборки или эксплуатации
    download_link = models.URLField()  # Ссылка на скачивание дополнительной информации или чертежа
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Цена самолёта


# Модель для описания комплектующих или компонентов самолёта
class Component(models.Model):
    name = models.CharField(max_length=255)  # Название компонента
    description = models.TextField()  # Описание компонента
    stock = models.PositiveIntegerField()  # Количество доступных единиц на складе
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена компонента
    category = models.CharField(max_length=100)  # Категория компонента (например, "сервоприводы" или "батарейки")


# Модель для хранения выбранных пользователем комплектующих
class SelectedParts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, который выбрал данные компоненты
    part = models.ForeignKey(Component, on_delete=models.CASCADE)  # Выбранный компонент
    quantity = models.IntegerField()  # Количество выбранных единиц компонента

    def __str__(self):
        return f"{self.user.username} selected {self.quantity} of {self.part.name}"  # Строковое представление


# Модель для корзины пользователя, связана один-к-одному с пользователем
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')  # Пользователь, владелец корзины
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания корзины

    def __str__(self):
        return f"{self.user.username}'s Cart"  # Строковое представление


# Модель для позиции в корзине, связана с конкретным компонентом и корзиной
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')  # Ссылка на корзину
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True,
                                  blank=True)  # Компонент, добавленный в корзину
    quantity = models.IntegerField(default=1)  # Количество выбранного компонента

    def __str__(self):
        return f"{self.cart.user.username} - {self.component}"  # Строковое представление
