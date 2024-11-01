from django.contrib import admin
from .models import Component, CartItem, Documentation, PlanePart, SelectedParts, ReadyKit, Cart

admin.site.register(CartItem)
admin.site.register(Documentation)
admin.site.register(PlanePart)
admin.site.register(SelectedParts)
admin.site.register(Component)
admin.site.register(ReadyKit)
admin.site.register(Cart)
