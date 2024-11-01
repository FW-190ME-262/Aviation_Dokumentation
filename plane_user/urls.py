from django.urls import path
from .views import PlaneDocumentationView, AvailablePartsListView, AddSelectedPartsView, SelectedPartsListView, \
    CartView, AddReadyKitToCartView, AddSelectedPartsToCartView, RemoveCartItemView

urlpatterns = [
    path('planes/<int:plane_id>/documentation/', PlaneDocumentationView.as_view(), name='plane-documentation'),
    path('parts/available/', AvailablePartsListView.as_view(), name='available-parts'),
    path('parts/select/', AddSelectedPartsView.as_view(), name='select-parts'),
    path('parts/selected/', SelectedPartsListView.as_view(), name='selected-parts'),
    path('cart/', CartView.as_view(), name='cart-detail'),
    path('cart/add-ready-kit/<int:kit_id>/', AddReadyKitToCartView.as_view(), name='add-ready-kit'),
    path('cart/add-selected-part/<int:part_id>/', AddSelectedPartsToCartView.as_view(), name='add-selected-part'),
    path('cart/remove-item/<int:item_id>/', RemoveCartItemView.as_view(), name='remove-cart-item'),
]
