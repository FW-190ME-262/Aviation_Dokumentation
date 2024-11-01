

from rest_framework import generics

from .serializers import PlanePartSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PlanePart, SelectedParts
from .serializers import SelectedPartsSerializer

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Cart, CartItem, ReadyKit, SelectedParts
from django.contrib.auth.models import User, Plane

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem, ReadyKit, SelectedParts
from .serializers import CartSerializer, CartItemSerializer, ReadyKitSerializer, SelectedPartsSerializer
from django.shortcuts import get_object_or_404


class CartView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddReadyKitToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, kit_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        ready_kit = get_object_or_404(ReadyKit, id=kit_id)
        CartItem.objects.create(cart=cart, ready_kit=ready_kit, quantity=1)
        return Response({"message": "Ready kit added to cart"}, status=status.HTTP_201_CREATED)


class AddSelectedPartsToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, part_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        selected_part = get_object_or_404(SelectedParts, id=part_id)
        CartItem.objects.create(cart=cart, selected_part=selected_part, quantity=1)
        return Response({"message": "Selected part added to cart"}, status=status.HTTP_201_CREATED)


class RemoveCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
        return Response({"message": "Item removed from cart"}, status=status.HTTP_204_NO_CONTENT)


class CartView(View):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = cart.items.all()
        return render(request, 'cart/cart_detail.html', {'cart': cart, 'items': items})


class AddReadyKitToCartView(View):
    def post(self, request, kit_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        ready_kit = get_object_or_404(ReadyKit, id=kit_id)
        CartItem.objects.create(cart=cart, ready_kit=ready_kit, quantity=1)
        return redirect('cart-detail')


class AddSelectedPartsToCartView(View):
    def post(self, request, part_id):
        cart, created = Cart.objects.get_or_create(user=request.user)
        selected_part = get_object_or_404(SelectedParts, id=part_id)
        CartItem.objects.create(cart=cart, selected_part=selected_part, quantity=1)
        return redirect('cart-detail')


class RemoveCartItemView(View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.delete()
        return redirect('cart-detail')


class AddSelectedPartsView(APIView):
    def post(self, request):
        serializer = SelectedPartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Part added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvailablePartsListView(generics.ListAPIView):
    queryset = PlanePart.objects.all()
    serializer_class = PlanePartSerializer


class AddSelectedPartsView(APIView):
    def post(self, request):
        serializer = SelectedPartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Part added successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaneDocumentationView(APIView):
    def get(self, request, plane_id):
        try:
            plane = Plane.objects.get(id=plane_id)
            documentation = plane.documentation  # поле с документацией в модели самолёта
            return Response({"documentation": documentation})
        except Plane.DoesNotExist:
            return Response({"error": "Plane not found"}, status=404)


class SelectedPartsListView(APIView):
    def get(self, request):
        selected_parts = SelectedParts.objects.filter(user=request.user)
        parts_data = [{"part": sp.part.name, "quantity": sp.quantity} for sp in selected_parts]
        return Response({"selected_parts": parts_data})
