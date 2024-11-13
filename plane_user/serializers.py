from rest_framework import serializers
from .models import Cart, CartItem, SelectedParts, Component, Plane


# Сериализатор для компонента самолета (деталь, запчасть)
class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'description', 'stock', 'price', 'category']


# Сериализатор для выбранных пользователем комплектующих
class SelectedPartsSerializer(serializers.ModelSerializer):
    part = serializers.PrimaryKeyRelatedField(queryset=Component.objects.all())  # Указываем компонент как ForeignKey

    class Meta:
        model = SelectedParts
        fields = ['id', 'part', 'quantity']


# Сериализатор для элемента корзины (каждая позиция в корзине)
class CartItemSerializer(serializers.ModelSerializer):
    component = ComponentSerializer(read_only=True)  # Вложенный сериализатор для компонента
    selected_part = SelectedPartsSerializer(read_only=True)  # Вложенный сериализатор для выбранных частей

    class Meta:
        model = CartItem
        fields = ['id', 'component', 'selected_part',
                  'quantity']  # ID элемента корзины, компонент, выбранная часть и количество


# Сериализатор для корзины пользователя
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # Вложенный сериализатор для списка элементов корзины

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']  # ID корзины, пользователь и список элементов


# Сериализатор для добавления комментариев к модели самолета (если поле 'comment' существует)
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'name',
                  'comment']  # Включает ID самолета, его имя и комментарий; убедитесь, что поле 'comment' добавлено в модель Plane