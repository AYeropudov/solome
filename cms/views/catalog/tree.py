from datetime import time

from shop.models import Catalog, CatalogTag, CatalogImage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View


class TreeView(View):
    def get(self, request):
        roots = Catalog.objects.root_nodes()
        menu_tree = []
        for root in roots:
            menu_tree.append({
                'title': root.title,
                'code': root.code,
                'child': root.get_children(),
                'img': root.catalogimage_set.all(),
                'pk': root.pk
            })
        return render(request=request, template_name='cms/catalog/tree.html', context={"tree": menu_tree})

    def post(self, request, cat_id):
        if cat_id:
            return self.put(request=request, cat_id=cat_id)
        else:
            pass
        return JsonResponse(data={"tic": time}, status=200)

    def put(self, request, cat_id):
        params = request.POST
        return JsonResponse(data={"tic": 123}, status=200)
