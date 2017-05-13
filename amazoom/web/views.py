import requests
import json

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView

from .models import Product


class ProductListView(TemplateView):
    template_name = 'product_list.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['object_list'] = requests.get('http://inventario:8001/api/product/list').json()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
    	url = 'http://pagos:8003/api/payment/%s/' % request.POST['pk']
    	print(json.dumps(request.POST))
    	context = requests.post(url, data=dict(request.POST))
    	print(context)
    	print(context.json())
    	return HttpResponse(context)

