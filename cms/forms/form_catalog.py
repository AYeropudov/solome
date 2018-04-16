from django.forms import ModelForm
from shop.models import Catalog


class FormCatalog(ModelForm):
    class Meta:
        model = Catalog
        fields = ['title', 'parent', 'code']
