from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Maintenance(View):

    def get(self, request):
        breadcrumbs = [
            {
                "uri": "/",
                "title": "Главная"
            },
            {
                "uri": "#",
                "title": "Технические работы"
            }
        ]
        return render(
            request=request,
            template_name='maintanance.html',
            context={"is_breadcrumbs": True, "breadcrumbs": breadcrumbs}
        )
        # return HttpResponse("Hello, world. You're at the about.")
