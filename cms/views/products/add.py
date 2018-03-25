from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from shop.models import Product, Catalog, ProductClass


class ProductsAddView(View):
    def get(self, request):
        product = None
        catalogs = Catalog.objects.all()
        pclasess = ProductClass.objects.all()
        return render(request=request, template_name='cms/products/add.html',
                      context={"title": "Товары", "product": product, "catalogs": catalogs, "product_class": pclasess})

    def post(self, request):

        return render(request=request, template_name='cms/products/add.html',
                      context={"title": "Товары", "product": None})
