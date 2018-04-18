from django.shortcuts import render
from django.views import View
from shop.models import Product

class QuickViewProduct(View):

    def get(self,request, p_code):
        _context = dict()
        try:
            product = Product.objects.get(pk=p_code)
            _context['product'] = product
        except Product.DoesNotExist:
            return render(request=request, template_name='')
        return render(request=request, template_name='modal-product.html', context=_context)