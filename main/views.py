from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.views import APIView

from .models import Country, Region, District, CityVillage, Course, Lesson, EducationalMaterial

from rest_framework import status
from .serializers import PlaneSerializer, TutorialSerializer, RegisterSerializer, CountrySerializer, RegionSerializer, \
    DistrictSerializer, CityVillageSerializer, CourseSerializer, LessonSerializer, EducationalMaterialSerializer, \
    CommentSerializer, RatingSerializer
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Plane, Tutorial


class PlaneDocumentationView(View):
    def get(self, request, plane_id):
        plane = get_object_or_404(Plane, id=plane_id)
        # Получаем все связанные документы для самолета
        documentation = plane.documentations.all()  # Используем related_name="documentations"
        documentation_data = [
            {"title": doc.title, "content": doc.content} for doc in documentation
        ]
        return JsonResponse({"plane_id": plane_id, "documentation": documentation_data})


# API для учебных материалов
class TutorialListView(generics.ListAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class TutorialDetailView(generics.RetrieveAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


# API для корзины
class CartItemListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


# Home
class All_planeListView(generics.ListAPIView):
    queryset = Plane.objects.all().order_by('-date_publications')[:3]  # Берем 3 самых новых самолета
    serializer_class = PlaneSerializer


class PlaneListView(generics.ListAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


# View  id
class PlaneDetailView(generics.RetrieveAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


# View для добавления комментариев
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Только авторизованные пользователи могут оставлять комментарии

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Сохраняем пользователя, который оставил комментарий


# View для выставления оценок
class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]  # Только авторизованные пользователи могут выставлять оценки

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# View for retrieving all countries
class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class RegionListByCountryView(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get_queryset(self):
        country_id = self.kwargs['country_id']
        return Region.objects.filter(country_id=country_id)


class DistrictListByRegionView(generics.ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return District.objects.filter(region_id=region_id)


class CityVillageListByDistrictView(generics.ListAPIView):
    serializer_class = CityVillageSerializer

    def get_queryset(self):
        district_id = self.kwargs['district_id']
        return CityVillage.objects.filter(district_id=district_id)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Регистрация прошла успешно!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommenteView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        plane_id = self.kwargs['plane_id']
        plane = Plane.objects.get(id=plane_id)
        serializer.save(plane=plane, user=self.request.user)


class RatingView(APIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        plane_id = self.kwargs['plane_id']
        plane = Plane.objects.get(id=plane_id)
        serializer.save(plane=plane, user=self.request.user)


class CheckoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        # Логика оформления заказа (например, создание записи о заказе)
        # Очистка корзины после оформления
        cart_items.delete()
        return Response({"message": "Order placed successfully!"}, status=status.HTTP_201_CREATED)


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# View to get detailed information about a specific lesson
import logging

logger = logging.getLogger(__name__)
class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    print(serializer_class)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info(f"Retrieved lesson: {instance}")
        serializer = self.get_serializer(instance)
        logger.info(f"Serialized data: {serializer.data}")
        return Response(serializer.data)

# View to get detailed information about a specific educational material
class EducationalMaterialDetailView(generics.RetrieveAPIView):
    queryset = EducationalMaterial.objects.all()
    serializer_class = EducationalMaterialSerializer





class CheckoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum([item.plane.price for item in cart_items])

        profile = request.user.profile
        if profile.balance >= total_price:
            profile.balance -= total_price
            profile.save()
            # Удаляем все элементы корзины
            cart_items.delete()
            return Response({"message": "Purchase successful!", "balance": profile.balance}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Insufficient balance!"}, status=status.HTTP_400_BAD_REQUEST)
