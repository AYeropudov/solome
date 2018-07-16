from django.forms import ModelForm
from shop.models import Tag


class FormTag(ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'code']
