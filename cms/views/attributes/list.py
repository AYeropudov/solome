from cms.adapters.exceptions import AttributeNotFoundException, AttributeSaveException
from shop.models import AttributeForProduct
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from cms.adapters import AdapterAttribute


class Attributes(View):

    def get(self, request, attr_id=None):
        attributes = AttributeForProduct.objects.all()
        return render(request=request, template_name='cms/attributes/list.html', context={"list": attributes})

    def post(self, request, attr_id=None):
        if attr_id:
            return self.put(request=request, attr_id=attr_id)
        else:
            try:
                AdapterAttribute.create(post_data=request.POST)
            except AttributeSaveException as e:
                return JsonResponse(data={"error": "validation", "errors": e.errors}, status=400)
        return JsonResponse(data={"tic": 111}, status=200)

    def put(self, request, attr_id):
        params = request.POST
        try:
            AdapterAttribute.update(post_data=params, attribute=attr_id)
            return JsonResponse(data={"tic": 123}, status=200)
        except AttributeNotFoundException:
            return JsonResponse(data={"error": "Catalog not found"}, status=404)
        except AttributeSaveException as e:
            return JsonResponse(data={"error": "validation", "errors": e.errors}, status=400)
