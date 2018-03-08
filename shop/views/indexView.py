from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request=request, template_name='index.html', context={"is_breadcrumbs": False, "landing": True})
        # return HttpResponse("Hello, world. You're at the index.")