# from django.urls import path
# from .views import (
#     CountryListView,
#     RegionListByCountryView,
#     DistrictListByRegionView,
#     CityVillageListByDistrictView,
#     PlaneListView, All_planeListView,
#     PlaneDetailView, CommentCreateView, RatingCreateView, TutorialListView, TutorialDetailView, CartItemListView,
#     CartItemDetailView, CheckoutView, CourseListView, CourseDetailView, LessonDetailView, EducationalMaterialDetailView
# )
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .views import RegisterView
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     #Обрабатывает завершение заказа (оплата и оформление покупки
#     path('api/checkout/', CheckoutView.as_view(), name='checkout'),
#     # Предоставляет список всех курсов, доступных на платформе.
#     path('courses/', CourseListView.as_view(), name='course-list'),
#     # Предоставляет подробности конкретного курса по его ID (pk).
#     path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
#     # Позволяет получить полную информацию по уроку в конкретном курсе по его ID (pk).
#     path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
#     # Дает доступ к конкретному учебному материалу, связанному с уроком или курсом.
#     path('materials/<int:pk>/', EducationalMaterialDetailView.as_view(), name='material-detail'),
#     # Возвращает список всех обучающих руководств (туториалов) в системе.
#     path('api/tutorials/', TutorialListView.as_view(), name='tutorial-list'),
#     # Возвращает подробности конкретного обучающего руководства по его ID (pk).Возвращает список всех обучающих руководств (туториалов) в системе.
#     path('api/tutorials/<int:pk>/', TutorialDetailView.as_view(), name='tutorial-detail'),
#     #Показывает детали конкретного руководства по его ID (pk).
#     path('api/cart/', CartItemListView.as_view(), name='cart-list'),
#     # Отображает список товаров или курсов, которые добавлены в корзину пользователя.
#     path('api/cart/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
#     # Позволяет увидеть детали определенного товара в корзине.
#     path('planes/', PlaneListView.as_view(), name='plane-list'),
#     # Отображает список всех доступных моделей самолетов.
#     path('planes/<int:pk>/', PlaneDetailView.as_view(), name='plane-detail'),
#     # Предоставляет информацию по конкретной модели самолета по её ID (pk).
#     path('planes/<int:plane_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
#     # Позволяет пользователю оставить комментарий к конкретной модели самолета.
#     path('planes/<int:plane_id>/ratings/', RatingCreateView.as_view(), name='rating-create'),
#     # Позволяет пользователю оценить конкретную модель самолета.
#     path('all_plane/', All_planeListView.as_view(), name='all_plane'),
#     # Отображает общий список всех самолетов в системе.
#     path('home/', PlaneListView.as_view(), name='plane-home'),
#     # Стартовая страница с отображением списка самолетов, возможно, с дополнительной информацией или фильтрацией.
#     path("registration/", RegisterView.as_view()),
#     # Обеспечивает регистрацию нового пользователя.
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # Точка для получения JWT-токена для аутентификации пользователей.
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     # Точка для обновления существующего токена, когда он истекает.
#     path('countries/', CountryListView.as_view(), name='country-list'),
#     # Отображает список стран.
#     path('countries/<int:country_id>/regions/', RegionListByCountryView.as_view(), name='region-list-by-country'),
#     # Возвращает список регионов внутри конкретной страны по её ID (country_id).
#     path('regions/<int:region_id>/districts/', DistrictListByRegionView.as_view(), name='district-list-by-region'),
#     # Возвращает список районов внутри определенного региона.
#     path('districts/<int:district_id>/cities-villages/', CityVillageListByDistrictView.as_view(),
#          name='city-village-list-by-district'),
#
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    CountryListView, RegionListByCountryView, DistrictListByRegionView, CityVillageListByDistrictView,
    PlaneListView, All_planeListView, PlaneDetailView, CommentCreateView, RatingCreateView,
    TutorialListView, TutorialDetailView, CartItemListView, CartItemDetailView, CheckoutView,
    CourseListView, CourseDetailView, LessonDetailView, EducationalMaterialDetailView, RegisterView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Processes checkout (payment and order placement)
    path('api/checkout/', CheckoutView.as_view(), name='checkout'),

    # Provides a list of all available courses
    path('courses/', CourseListView.as_view(), name='course-list'),

    # Provides details for a specific course by its ID (pk)
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # Provides detailed information about a specific lesson by its ID (pk)
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),

    # Access to a specific educational material associated with a lesson or course
    path('materials/<int:pk>/', EducationalMaterialDetailView.as_view(), name='material-detail'),

    # Returns a list of all tutorials in the system
    path('api/tutorials/', TutorialListView.as_view(), name='tutorial-list'),

    # Provides details of a specific tutorial by its ID (pk)
    path('api/tutorials/<int:pk>/', TutorialDetailView.as_view(), name='tutorial-detail'),

    # Shows the user's cart contents (all added items)
    path('api/cart/', CartItemListView.as_view(), name='cart-list'),

    # Provides details of a specific item in the user's cart by its ID (pk)
    path('api/cart/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),

    # Displays a list of all available planes
    path('planes/', PlaneListView.as_view(), name='plane-list'),

    # Provides information on a specific plane model by its ID (pk)
    path('planes/<int:pk>/', PlaneDetailView.as_view(), name='plane-detail'),

    # Allows users to comment on a specific plane model by its ID
    path('planes/<int:plane_id>/comments/', CommentCreateView.as_view(), name='comment-create'),

    # Allows users to rate a specific plane model by its ID
    path('planes/<int:plane_id>/ratings/', RatingCreateView.as_view(), name='rating-create'),

    # Displays a list of all planes in the system
    path('all_plane/', All_planeListView.as_view(), name='all_plane'),

    # Home page listing planes, possibly with filtering options
    path('home/', PlaneListView.as_view(), name='plane-home'),

    # User registration endpoint
    path("registration/", RegisterView.as_view()),

    # JWT token endpoints for authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Location-related views: country, region, district, city/village
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('countries/<int:country_id>/regions/', RegionListByCountryView.as_view(), name='region-list-by-country'),
    path('regions/<int:region_id>/districts/', DistrictListByRegionView.as_view(), name='district-list-by-region'),
    path('districts/<int:district_id>/cities-villages/', CityVillageListByDistrictView.as_view(),
         name='city-village-list-by-district'),
]

# Serves media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
