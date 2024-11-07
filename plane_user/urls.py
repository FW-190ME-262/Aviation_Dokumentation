from django.urls import path
from .views import AddSelectedPartsView, SelectedPartsListView, \
    CartView, AddSelectedPartsToCartView, RemoveCartItemView

urlpatterns = [
    path('parts/select/', AddSelectedPartsView.as_view(), name='select-parts'),
    path('parts/selected/', SelectedPartsListView.as_view(), name='selected-parts'),
    path('cart/', CartView.as_view(), name='cart-detail'),
    path('cart/add-selected-part/<int:part_id>/', AddSelectedPartsToCartView.as_view(), name='add-selected-part'),
    path('cart/remove-item/<int:item_id>/', RemoveCartItemView.as_view(), name='remove-cart-item'),
]
