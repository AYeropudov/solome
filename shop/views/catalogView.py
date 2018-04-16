from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from shop.adapters import CatalogAdapter


class CatalogView(View):
    def get(self, request):

        breadcrumbs = [
            {
                "uri": "/",
                "title": "Главная"
            },
            {
                "uri": "#",
                "title": "Каталог"
            }
        ]

        try:
            catalog_nodes = CatalogAdapter.get_catalog_nodes()
        except:
            catalog_nodes = []
        return render(
            request=request,
            template_name='catalog.html',
            context={"is_breadcrumbs": True, "breadcrumbs": breadcrumbs, "nodes": catalog_nodes}
        )
        # return HttpResponse("Hello, world. You're at the CatalogView.")

