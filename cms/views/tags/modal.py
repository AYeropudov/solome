from django.shortcuts import render, get_object_or_404
from django.views import View
from shop.models import Tag


class ModalTags(View):

    def get(self, request, tag_id=None):

        if tag_id:
            if tag_id == 'tagging':
                return render(
                    request=request,
                    template_name='cms/tags/modal-mass-tagging.html',
                    context={"tags": Tag.objects.all()}
                )
            tag = get_object_or_404(Tag, pk=tag_id)
            return render(
                request=request,
                template_name='cms/tags/modal-edit.html',
                context={"item": tag}
            )
        else:
            return render(
                request=request,
                template_name='cms/tags/modal-add.html',
                context={}
            )
