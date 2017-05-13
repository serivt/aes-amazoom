from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
	url(r'^shipping/list/$', ShippingList.as_view(), name='shipping_list'),
	url(r'^shipping/$', CreateShipping.as_view(),
		name='retrieve_shipping'),
]
