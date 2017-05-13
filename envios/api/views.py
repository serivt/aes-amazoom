from rest_framework import generics


from .models import Shipping
from .serializers import ShippingSerializer


class ShippingList(generics.ListAPIView):
	serializer_class = ShippingSerializer
	queryset = Shipping.objects.all()

class CreateShipping(generics.CreateAPIView):
	serializer_class = ShippingSerializer
	queryset = Shipping.objects.all()