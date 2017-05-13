from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()

class RetrieveProduct(generics.RetrieveAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()