from django.shortcuts import render
from django.views import View


class ItemView(View):

    @staticmethod
    def get(request, item_code):
        return render(request, 'detail-product.html', {"product": None, 'title': item_code})
