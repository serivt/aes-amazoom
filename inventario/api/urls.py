from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
	url(r'^product/list/$', ProductList.as_view(), name='product_list'),
	url(r'^product/(?P<pk>[0-9]+)/$', RetrieveProduct.as_view(), name='retrieve_product'),
]
