from django.db import transaction
from django.db import IntegrityError
from cms.adapters.exceptions import ProductException
from shop.models import Product, ProductClass, ProductImage, ProductToCatalog, Catalog
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from .adapter_product import AdapterProduct
from cms.forms import FormCatalog
from cms.adapters.exceptions import CatalogNotFound, CatalogSaveException


class AdapterCatalog:

    @classmethod
    def update(cls, catalog, raw_data, file=None):
        try:
            _instance = Catalog.objects.get(pk=catalog)
            to_save = FormCatalog(raw_data, instance=_instance)
            if to_save.is_valid():
                try:
                    to_save.full_clean()
                    to_save.save()
                    if file is not None:
                        for fl in file.getlist('image'):
                            image = _instance.catalogimage_set.all()
                            image = image[0]
                            image.link = fl
                            image.save()
                except IntegrityError:
                    raise CatalogSaveException()
        except Catalog.DoesNotExist:
            raise CatalogNotFound()

    @classmethod
    def create(cls, raw_data):
        try:
            to_save = FormCatalog(raw_data)
            if to_save.is_valid():
                try:
                    to_save.full_clean()
                    to_save.save()
                except IntegrityError:
                    raise CatalogSaveException()
        except Catalog.DoesNotExist:
            raise CatalogNotFound()
