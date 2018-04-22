from decimal import Decimal

from django.db import transaction
from django.db import IntegrityError
from cms.adapters.exceptions import ProductException
from shop.models import Product, ProductClass, ProductImage, ProductToCatalog, Catalog, ProductBrand
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


class AdapterProduct:
    @classmethod
    def create_new_product(cls, form_data, files):
        try:
            with transaction.atomic():
                product_class = None
                product_brand = None
                catalog = None
                try:
                    product_class = ProductClass.objects.get(pk=int(form_data['product_class']))
                except ProductClass.DoesNotExist as e:
                    raise ProductException('Не удалось найти такой вид товара')

                try:
                    catalog = Catalog.objects.get(pk=int(form_data['catalog']))
                except Catalog.DoesNotExist as e:
                    raise ProductException('Не удалось найти такой каталог')
                try:
                    product_brand = ProductBrand.objects.get(pk=int(form_data['product_brand']))
                except ProductBrand.DoesNotExist as e:
                    raise ProductException('Не удалось найти такой бренд')
                pr = form_data['price'].replace(",", ".")
                pr = float(pr)

                new_product = Product(
                    title=form_data['title'],
                    product_class=product_class,
                    description=form_data['description'],
                    brand=product_brand,
                    code=form_data['code'],
                    price=pr,
                    is_delete=False,
                    is_featured=True
                )
                try:
                    new_product.clean_fields()
                    new_product.save()
                except ValidationError as e:
                    tmp = e
                    raise ProductException(message='validation errors', errors=e.message_dict)
                try:
                    ProductToCatalog.objects.create(product=new_product, catalog=catalog)
                    if catalog.parent:
                        ProductToCatalog.objects.create(product=new_product, catalog=catalog.parent)
                except IntegrityError as e:
                    raise ProductException('Не удалось добавить товар к каталогу')
                try:
                    for file in files.getlist('images'):
                        ProductImage.objects.create(
                            product=new_product,
                            link=file,
                            is_delete=False
                        )
                except IntegrityError as e:
                    raise ProductException('Не удалось загрузить картинки')
                return new_product
        except ProductException as e:
            raise e
        except IntegrityError as e:
            raise ProductException('Не удалось сохранить товар в БД')

    @classmethod
    def update_product(cls, form_data, files, product_id):
        try:
            with transaction.atomic():
                product_class = None
                product_brand = None
                catalog = None
                try:
                    product_class = ProductClass.objects.get(pk=int(form_data['product_class']))
                except ProductClass.DoesNotExist as e:
                    raise ProductException('Не удалось найти такой вид товара')

                try:
                    catalog = Catalog.objects.get(pk=int(form_data['catalog']))
                except Catalog.DoesNotExist as e:
                    raise ProductException('Не удалось найти такой каталог')

                try:
                    product_brand = ProductBrand.objects.get(pk=int(form_data['product_brand']))
                except ProductBrand.DoesNotExist as e:
                    raise ProductException('Не удалось найти такой бренд')

                try:
                    product_to_update = Product.objects.get(pk=product_id)
                    product_to_update.title = form_data['title']
                    product_to_update.description = form_data['description']
                    product_to_update.product_class = product_class
                    product_to_update.brand = product_brand
                    product_to_update.code = form_data['code']
                    pr = form_data['price'].replace(",", ".")
                    pr = float(pr)
                    product_to_update.price = float(pr)
                    try:
                        product_to_update.clean_fields()
                        product_to_update.save()
                    except ValidationError as e:
                        raise ProductException(message='validation errors', errors=e.message_dict)
                    try:
                        ProductToCatalog.objects.filter(product=product_to_update).delete()
                    except IntegrityError as e:
                        raise ProductException('can\'t update catalog')
                    try:
                        ProductToCatalog.objects.create(product=product_to_update, catalog=catalog)
                        if catalog.parent:
                            ProductToCatalog.objects.create(product=product_to_update, catalog=catalog.parent)
                    except IntegrityError as e:
                        raise ProductException('Не удалось добавить товар к каталогу')
                    try:
                        for file in files.getlist('images'):
                            ProductImage.objects.create(
                                product=product_to_update,
                                link=file,
                                is_delete=False
                            )
                    except IntegrityError as e:
                        raise ProductException('Не удалось загрузить картинки')
                    return product_to_update

                except Product.DoesNotExist as e:
                    raise ProductException('can\'t find product to update')

        except ProductException as e:
            raise e
