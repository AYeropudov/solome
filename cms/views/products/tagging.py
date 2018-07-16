from django.http import JsonResponse
from django.views import View
import json
from shop.models import Product, Tag, ProductTag
from django.db.utils import IntegrityError


class TaggingProducts(View):
    def post(self, request):
        data = json.loads(request.body)
        products_ids = data.get('products')
        tags_ids = data.get('tags')
        tags = Tag.objects.filter(pk__in=tags_ids)
        products = Product.objects.filter(pk__in=products_ids)
        for product in products:
            for tag in tags:
                try:
                    ProductTag.objects.create(tag=tag, product=product)
                except IntegrityError as e:
                    pass
        return JsonResponse(data={"result": "suucess"}, status=200)
