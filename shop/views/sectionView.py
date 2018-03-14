from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class SectionView(View):
    def get(self, request, section_code):

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
                "title": "Какая-то категория " + section_code
            }
        ]
        return render(
            request=request,
            template_name='section.html',
            context={"is_breadcrumbs": True, "breadcrumbs": breadcrumbs}
        )
        # return HttpResponse("Hello, world. You're at the CatalogView.")