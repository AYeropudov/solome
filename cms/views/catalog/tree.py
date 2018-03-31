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
                'img': root.catalogimage_set.all()
            })
        return render(request=request, template_name='cms/catalog/tree.html', context={"tree": menu_tree})

    def post(self, request):
        pass
