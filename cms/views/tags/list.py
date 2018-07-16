from cms.adapters.exceptions import AttributeNotFoundException, AttributeSaveException
from shop.models import Tag
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from cms.adapters import AdapterTags


class Tags(View):

    def get(self, request, tag_id=None):
        tags = Tag.objects.all()
        return render(request=request, template_name='cms/tags/list.html', context={"list": tags})

    def post(self, request, tag_id=None):
        if tag_id:
            return self.put(request=request, attr_id=tag_id)
        else:
            try:
                AdapterTags.create(post_data=request.POST)
            except AttributeSaveException as e:
                return JsonResponse(data={"error": "validation", "errors": e.errors}, status=400)
        return JsonResponse(data={"tic": 111}, status=200)

    def put(self, request, attr_id):
        params = request.POST
        try:
            AdapterTags.update(post_data=params, attribute=attr_id)
            return JsonResponse(data={"tic": 123}, status=200)
        except AttributeNotFoundException:
            return JsonResponse(data={"error": "Catalog not found"}, status=404)
        except AttributeSaveException as e:
            return JsonResponse(data={"error": "validation", "errors": e.errors}, status=400)
