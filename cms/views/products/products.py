from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from shop.models import Product


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()

        return render(request=request, template_name='cms/products/list.html',
                      context={"title": "Товары", "list": products})
