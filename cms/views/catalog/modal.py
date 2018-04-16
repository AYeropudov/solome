from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from shop.models import Catalog


class CatalogsModals(View):

    def get(self, request, type_modal):
        catalog = None
        if type_modal != 'createRoot':
            cat_id = int(request.GET.get("catId", 0))
            catalog = get_object_or_404(Catalog, pk=cat_id)

        if type_modal == 'editCat':
            if catalog.parent is None:

                return render(request=request,
                              template_name="cms/catalog/modal-edit-root.html",
                              context={"element": catalog})
            else:
                parents = Catalog.objects.root_nodes()
                return render(request=request,
                              template_name="cms/catalog/modal-edit-child.html",
                              context={"element": catalog, "parents": parents})

        elif type_modal == 'createSubCat':
            return render(request=request, template_name="cms/catalog/modal-add-sub.html", context={"parent": catalog})

        elif type_modal == 'createRoot':
            return render(request=request, template_name="cms/catalog/modal-add.html", context={})

        return HttpResponse(content=b"<h3>Ops...</h3>")
