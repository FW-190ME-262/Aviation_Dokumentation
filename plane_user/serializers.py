from rest_framework import serializers
from .models import Cart, CartItem, SelectedParts, Component, Plane

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', 'description', 'stock', 'price', 'category']


class SelectedPartsSerializer(serializers.ModelSerializer):
    part = ComponentSerializer(read_only=True)

    class Meta:
        model = SelectedParts
        fields = ['id', 'part', 'quantity']


class CartItemSerializer(serializers.ModelSerializer):
    component = ComponentSerializer(read_only=True)
    selected_part = SelectedPartsSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'component', 'selected_part', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'name', 'comment']  # Убедитесь, что поле 'comment' существует в модели Plane
