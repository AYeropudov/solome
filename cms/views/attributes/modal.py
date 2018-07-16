from django.shortcuts import render, get_object_or_404
from django.views import View
from shop.models import AttributeForProduct


class ModalAttribute(View):

    def get(self, request, attr_id=None):
        _choices = AttributeForProduct.CAST_CHOICES
        if attr_id:
            attr = get_object_or_404(AttributeForProduct, pk=attr_id)
            return render(
                request=request,
                template_name='cms/attributes/modal-edit.html',
                context={"item": attr, 'choices': _choices}
            )
        else:
            return render(
                request=request,
                template_name='cms/attributes/modal-add.html',
                context={'choices': _choices}
            )
