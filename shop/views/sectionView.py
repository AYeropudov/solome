from django.shortcuts import render
from django.views import View
from shop.adapters import CatalogAdapter
from shop.Exceprions import CatalogDoesNotExist


class SectionView(View):
    @staticmethod
    def get(request, section_code):
        try:
            section = CatalogAdapter.get_section_by_slug(section_code)
            section_title = section.title
        except CatalogDoesNotExist:
            section_title = 'Нету такого...'
            section = None

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
            context={"is_breadcrumbs": False, "breadcrumbs": breadcrumbs, "section": section}
        )


