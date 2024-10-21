from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .models import Country, Profile, Region, District, CityVillage  # Adjust according to your actual model names
from .serializers import CountrySerializer, RegionSerializer, DistrictSerializer, CityVillageSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Plane, Comment, Rating
from .serializers import PlaneSerializer, CommentSerializer, RatingSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import Plane
from .serializers import PlaneSerializer


class All_planeListView(generics.ListAPIView):
    queryset = Plane.objects.all().order_by('-date_publications')[:3]  # Берем 3 самых новых самолета
    serializer_class = PlaneSerializer


class PlaneListView(generics.ListAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


# View для получения деталей о самолете по ID
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
