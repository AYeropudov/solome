from cms.adapters.exceptions import CatalogNotFound, CatalogSaveException
from shop.models import Catalog, CatalogTag, CatalogImage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from cms.adapters import AdapterCatalog


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

    def post(self, request, cat_id=None):
        if cat_id:
            return self.put(request=request, cat_id=cat_id)
        else:
            try:
                AdapterCatalog.create(raw_data=request.POST)
            except CatalogNotFound:
                return JsonResponse(data={"error": "Catalog not found"}, status=404)
            except CatalogSaveException:
                return JsonResponse(data={"error": 'validation'}, status=400)

        return JsonResponse(data={"tic": 111}, status=200)

    def put(self, request, cat_id):
        params = request.POST
        try:
            AdapterCatalog.update(raw_data=params, catalog=cat_id, file=request.FILES)
            return JsonResponse(data={"tic": 123}, status=200)
        except CatalogNotFound:
            return JsonResponse(data={"error": "Catalog not found"}, status=404)
        except CatalogSaveException:
            return JsonResponse(data={"error": 'validation'}, status=400)
