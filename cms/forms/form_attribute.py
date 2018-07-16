from django.forms import ModelForm
from shop.models import AttributeForProduct


class FormAttribute(ModelForm):
    class Meta:
        model = AttributeForProduct
        fields = ['title', 'code', 'cast_type']
