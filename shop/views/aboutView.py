from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class AboutView(View):

    def get(self, request):
        breadcrumbs = [
            {
                "uri": "/",
                "title": "Главная"
            },
            {
                "uri": "#",
                "title": "О компании"
            }
        ]
        return render(
            request=request,
            template_name='about.html',
            context={"is_breadcrumbs": True, "breadcrumbs": breadcrumbs}
        )
        # return HttpResponse("Hello, world. You're at the about.")
