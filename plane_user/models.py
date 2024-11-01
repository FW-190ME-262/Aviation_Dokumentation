from django.db import models
# from rest_framework.authtoken.admin import User
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


# Модель для комплектующих
class Component(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.PositiveIntegerField()  # Количество на складе
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # Тип, например, "сервоприводы", "батарейки"


# Модель для документации
class Documentation(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Описание или ссылка на файл
    plane_model = models.ForeignKey(Plane, on_delete=models.CASCADE)


class PlanePart(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name


class SelectedParts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    part = models.ForeignKey(PlanePart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} selected {self.quantity} of {self.part.name}"


# Модель для готовых наборов
class ReadyKit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# Модель корзины
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"


# Модель для товаров в корзине
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    ready_kit = models.ForeignKey(ReadyKit, on_delete=models.CASCADE, null=True, blank=True)  # готовый набор
    selected_part = models.ForeignKey('SelectedParts', on_delete=models.CASCADE, null=True,
                                      blank=True)  # выбранный комплектующий
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cart.user.username} - {self.ready_kit or self.selected_part}"


'докуменрация свагер'

#
# {
#     "id": 1,
#     "name": "сервопривод_12",
#     "description": "Система управления положением и его производными от времени, такими как скорость, механической системы. Она часто включает в себя серводвигатель и использует управление по замкнутому контуру для уменьшения ошибки в установившемся режиме и улучшения динамической характеристики. В управлении по замкнутому контуру для коррекции действия механизма используется отрицательная обратная связь с определением ошибок. В приложениях, контролирующих",
#     "quantity_in_stock": 10
# },
# {
#     "id": 2,
#     "name": "F60 Pro IV IIII Поколение 4 2207 1950KV 2550KV 5-6S бесщеточный двигатель T5146 T5150",
#     "description": "Новый T-двигатель F60 Pro IV IIII Поколение 4 2207 1950KV 2550KV 5-6S бесщеточный двигатель T5146 T5150 реквизит для RC FPV гоночного дрона",
#     "quantity_in_stock": 5
# },
# {
#     "id": 3,
#     "name": "Dupont 10 см",
#     "description": "Провода-перемычки Dupont 10 см 3 вида по 40 шт мама-мама, папа-папа, папа-мама для Arduino, STM32, NodeMCU, Raspberry Pi",
#     "quantity_in_stock": 50
# },
# {
#     "id": 4,
#     "name": "nRF24L01 + 2,4G 150M,",
#     "description": "Передатчик и приемник nRF24L01 + 2,4G 150M, беспроводной модуль трансивера, интерфейс IIC SPI для Arduino UAV, лодки, авто, электрические игрушки",
#     "quantity_in_stock": 15
# },
# {
#     "id": 5,
#     "name": "RCinpower GTS V3 1303 PLUS",
#     "description": "RCinpower GTS V3 1303 PLUS бесщеточный двигатель для 2-дюймового кругового самолета DJI O3 Mapper",
#     "quantity_in_stock": 10
#
