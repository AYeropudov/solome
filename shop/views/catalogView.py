from django.http import HttpResponse
from django.views import View


class CatalogView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the CatalogView.")