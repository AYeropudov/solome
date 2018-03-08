from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class AboutView(View):
    def get(self, request):
        return render(request=request, template_name='about.html', context={"is_breadcrumbs": True})
        # return HttpResponse("Hello, world. You're at the about.")