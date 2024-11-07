from django.contrib import admin
from .models import Component, CartItem,SelectedParts,  Cart

admin.site.register(CartItem)
admin.site.register(SelectedParts)
admin.site.register(Component)
admin.site.register(Cart)
