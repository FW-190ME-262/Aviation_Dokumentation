from django.urls import path
from .views import (
    CountryListView,
    RegionListByCountryView,
    DistrictListByRegionView,
    CityVillageListByDistrictView,
    PlaneListView, All_planeListView,
    PlaneDetailView, CommentCreateView, RatingCreateView, TutorialListView, TutorialDetailView, CartItemListView,
    CartItemDetailView, CheckoutView, CourseListView, CourseDetailView, LessonDetailView, EducationalMaterialDetailView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/checkout/', CheckoutView.as_view(), name='checkout'),

    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('materials/<int:pk>/', EducationalMaterialDetailView.as_view(), name='material-detail'),

    path('api/tutorials/', TutorialListView.as_view(), name='tutorial-list'),
    path('api/tutorials/<int:pk>/', TutorialDetailView.as_view(), name='tutorial-detail'),
    path('api/cart/', CartItemListView.as_view(), name='cart-list'),
    path('api/cart/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),

    path('planes/', PlaneListView.as_view(), name='plane-list'),
    path('planes/<int:pk>/', PlaneDetailView.as_view(), name='plane-detail'),
    path('planes/<int:plane_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('planes/<int:plane_id>/ratings/', RatingCreateView.as_view(), name='rating-create'),
    path('all_plane/', All_planeListView.as_view(), name='all_plane'),
    path('home/', PlaneListView.as_view(), name='plane-home'),
    path("registration/", RegisterView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('countries/', CountryListView.as_view(), name='country-list'),
    path('countries/<int:country_id>/regions/', RegionListByCountryView.as_view(), name='region-list-by-country'),
    path('regions/<int:region_id>/districts/', DistrictListByRegionView.as_view(), name='district-list-by-region'),
    path('districts/<int:district_id>/cities-villages/', CityVillageListByDistrictView.as_view(),
         name='city-village-list-by-district'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)