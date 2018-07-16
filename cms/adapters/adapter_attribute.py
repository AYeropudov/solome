from django.db import transaction
from django.db import IntegrityError
from cms.adapters.exceptions import AttributeNotFoundException, AttributeSaveException
from shop.models import AttributeForProduct
from cms.forms import FormAttribute


class AdapterAttribute:
    @classmethod
    def create(cls, post_data):
        to_save = FormAttribute(post_data)
        if to_save.is_valid():
            try:
                to_save.full_clean()
                to_save.save()
            except IntegrityError:
                raise AttributeError()

    @classmethod
    def update(cls, attribute,  post_data):
        try:
            _instance = AttributeForProduct.objects.get(pk=attribute)
            to_save = FormAttribute(post_data, instance=_instance)
            if to_save.is_valid():
                try:
                    to_save.full_clean()
                    to_save.save()
                except IntegrityError as e:
                    raise AttributeSaveException(str(e))
            else:
                raise AttributeSaveException(errors=to_save.errors)

        except AttributeForProduct.DoesNotExist:
            raise AttributeNotFoundException()
