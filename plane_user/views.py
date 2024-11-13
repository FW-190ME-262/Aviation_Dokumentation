from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import SelectedParts, Cart, CartItem
from .serializers import CartSerializer, SelectedPartsSerializer


# Добавление выбранного комплекта деталей в корзину
class AddSelectedPartsToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, part_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        selected_part = get_object_or_404(SelectedParts, id=part_id)
        # Изменим 'selected_part' на 'component' для правильного создания CartItem
        CartItem.objects.create(cart=cart, component=selected_part.part, quantity=1)
        return Response({"message": "Selected part added to cart"}, status=status.HTTP_201_CREATED)


# Удаление товара из корзины
class RemoveCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
        return Response({"message": "Item removed from cart"}, status=status.HTTP_204_NO_CONTENT)


# Просмотр корзины
class CartView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


# Добавление выбранных частей
class AddSelectedPartsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SelectedPartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Part added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Просмотр выбранных пользователем частей
class SelectedPartsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        selected_parts = SelectedParts.objects.filter(user=request.user)
        parts_data = [
            {
                "part_name": sp.part.name,
                "quantity": sp.quantity,
            }
            for sp in selected_parts
        ]
        return Response({"selected_parts": parts_data})
