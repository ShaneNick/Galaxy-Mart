from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product

# This view handles listing all categories and creating a new category.
# It inherits from ListCreateAPIView 
# It provides GET (list) and POST (create) actions without having to define them explicitly.
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()  # Defines the queryset that will be used to list categories.
    serializer_class = CategorySerializer  # Specifies the serializer class for serializing the queryset.

# This view is for retrieving (GET), updating (PUT/PATCH), and deleting (DELETE) a specific category instance.
# It inherits from RetrieveUpdateDestroyAPIView, providing the mentioned actions for a single model instance.
class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()  # The queryset includes all category instances.
    serializer_class = CategorySerializer  # Defines the serializer for the category instances, used for both input (update) and output (retrieve).

# Similar to the CategoryListCreateAPIView, this view is for listing all products and creating new ones.
# It uses ListCreateAPIView to provide a listing of all Product instances and an interface to create new Product instances.
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()  # The queryset that will be used to list or create Products.
    serializer_class = ProductSerializer  # The serializer class for product instances.

# This view handles the actions for a single product instance: retrieving it, updating it, or deleting it.
# It leverages the RetrieveUpdateDestroyAPIView for these actions on Product model instances.
class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()  # Defines the queryset for all product instances.
    serializer_class = ProductSerializer  # Specifies the serializer to use for serializing product data.