from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from shop.models import Catalog


class IndexView(View):
    def get(self, request):
        _context = {"products": [], "is_breadcrumbs": False, "landing": True, 'nodes': Catalog.objects.root_nodes()}
        for node in _context['nodes']:
            products = list(node.producttocatalog_set.all().order_by('?')[:4])
            _context['products'] = _context['products'] + products

        return render(request=request, template_name='index.html', context=_context)
        # return HttpResponse("Hello, world. You're at the index.")