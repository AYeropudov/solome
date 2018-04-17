from django.forms import ModelForm
from shop.models import Product


class FormProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']