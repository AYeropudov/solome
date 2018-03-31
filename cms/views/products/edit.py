from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from shop.models import Product, Catalog, ProductClass
from cms.adapters import AdapterProduct
from cms.adapters.exceptions import ProductException


class ProductsEditView(View):

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        nodes = product.producttocatalog_set.filter()
        catalog = None
        for node in nodes:
            if node.catalog.parent is not None:
                catalog = node.catalog.pk
        catalogs = Catalog.objects.all()
        pclasess = ProductClass.objects.all()
        return render(request=request, template_name='cms/products/edit.html',
                      context={"title_page": "Товары", "product": product, "catalogs": catalogs, "product_class_list": pclasess, 'catalog': catalog})

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        keys = request.POST.keys()
        prevalidate = {}
        for key in keys:
            if request.POST[key] == '':
                prevalidate[key] = 'Это обязательное поле'
        if len(prevalidate.keys()) > 0:
            return JsonResponse(data={"errors": prevalidate}, status=400)
        try:
            AdapterProduct.update_product(form_data=request.POST, files=request.FILES, product_id=product_id)
        except ProductException as e:
            _context = dict()
            _context['errors'] = e.errors
            return JsonResponse(data=_context, status=400)
        return JsonResponse(data={'ok': ""}, status=200)
