from .models import PlanePart

from rest_framework import serializers
from .models import Cart, CartItem, ReadyKit, SelectedParts


class PlanePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanePart
        fields = ['id', 'name', 'description', 'quantity_in_stock']


class SelectedPartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedParts
        fields = ['part', 'quantity']


class ReadyKitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyKit
        fields = ['id', 'name', 'description', 'price']


class SelectedPartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedParts
        fields = ['id', 'part', 'quantity']


class CartItemSerializer(serializers.ModelSerializer):
    ready_kit = ReadyKitSerializer(read_only=True)
    selected_part = SelectedPartsSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'ready_kit', 'selected_part', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
