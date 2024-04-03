from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem, Product
from .serializers import CartSerializer, CartItemSerializer

class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        product = get_object_or_404(Product, id=product_id)

        cart, _ = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, 
            product=product, 
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        response_detail = f"{quantity} x '{product.name}' added to cart."
        return Response({'detail': response_detail}, status=status.HTTP_200_OK)

class UpdateCartItemView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return self.queryset.filter(cart__user=self.request.user)

class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id, *args, **kwargs):
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        cart_item = get_object_or_404(CartItem, product_id=product_id, cart=cart)
        cart_item.delete()
        return Response({'detail': 'Item removed from cart.'}, status=status.HTTP_204_NO_CONTENT)

