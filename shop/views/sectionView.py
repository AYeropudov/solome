from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from shop.adapters import CatalogAdapter

class SectionView(View):
    def get(self, request, section_code):
        try:
            section = CatalogAdapter.get_section_by_slug(section_code)
            section_title = section.title
        except:
            section_title = 'Нету такого...'
            section= None

        breadcrumbs = [
            {
                "uri": "/",
                "title": "Главная"
            },
            {
                "uri": "/catalog",
                "title": "Каталог"
            },
            {
                "uri": "#",
                "title": "Какая-то категория " + section_title
            }
        ]

        return render(
            request=request,
            template_name='section.html',
            context={"is_breadcrumbs": True, "breadcrumbs": breadcrumbs}
        )
        # return HttpResponse("Hello, world. You're at the CatalogView.")