from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from shop.models import Product, Catalog, ProductClass, ProductBrand
from cms.adapters import AdapterProduct
from cms.adapters.exceptions import ProductException


class ProductsCopyView(View):

    def get(self, request):
        return JsonResponse(data={'ok': ""}, status=200)

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        try:
            _copied = AdapterProduct.copy_product(product_id=product_id)
            return JsonResponse(data={
                'ok': "",
                "location": reverse(
                    'cms.product.edit',
                    current_app=request.resolver_match.namespace,
                    kwargs={"product_id": _copied.pk})
            }, status=200)
        except ProductException as e:
            _context = dict()
            _context['errors'] = e.errors
            return JsonResponse(data=_context, status=400)
