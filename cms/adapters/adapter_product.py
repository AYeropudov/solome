from django.db import transaction
from django.db import IntegrityError
from cms.adapters.exceptions import ProductException
from shop.models import Product, ProductClass, ProductImage, ProductToCatalog, Catalog
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


class AdapterProduct:
    @classmethod
    def create_new_product(cls, form_data, files):
        try:
            with transaction.atomic():
                product_class = None
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
                    pr = float(form_data['price'])
                except:
                    pr = None
                new_product = Product(
                    title=form_data['title'],
                    product_class=product_class,
                    description=form_data['description'],
                    price=pr,
                    is_delete=False,
                    is_featured=True,
                )
                try:
                    new_product.clean_fields()
                    new_product.save()
                except ValidationError as e:
                    raise ProductException(message='validation errors', errors=e.message_dict)
                # new_product = Product.objects.create(
                #     title=form_data['title'],
                #     product_class = product_class,
                #     description = form_data['description'],
                #     price= float(form_data['price']),
                #     is_delete= False,
                #     is_featured= True,
                # )
                try:
                    ProductToCatalog.objects.create(product=new_product, catalog=catalog)
                    if(catalog.parent):
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
