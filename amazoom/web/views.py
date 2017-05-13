import requests

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Product


class ProductListView(TemplateView):
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['object_list'] = requests.get('http://inventario:8001/api/product/list').json()
        return context

