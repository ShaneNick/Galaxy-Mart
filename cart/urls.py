from django.urls import path
from .views import CartDetailView, AddToCartView, UpdateCartItemView, RemoveFromCartView

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('update-cart-item/<int:pk>/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('remove-from-cart/<int:product_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]
