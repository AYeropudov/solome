from django.db import models
import uuid
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def upload_to(instance, filename):
    filename = str(uuid.uuid1()) + "." + filename.split('.', 1)[-1]
    return 'uploads/photo/{}'.format(filename)


class ProductClass(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    has_variants = models.BooleanField(default=False, blank=True)
    is_delete = models.BooleanField(default=False, blank=True)


class Product(models.Model):
    product_class = models.ForeignKey(ProductClass, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300, db_index=True)
    description = models.TextField()
    is_featured = models.BooleanField(default=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default= 0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False, blank=True)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_index=True)
    override_price = models.DecimalField(blank=True, max_digits=12, decimal_places=2, default= 0.00)
    sku = models.CharField(max_length=300, db_index=True)
    is_delete = models.BooleanField(default=False, blank=True)
    is_featured = models.BooleanField(default=False, blank=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_index=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    ink = models.ImageField(upload_to=upload_to)
    full = ImageSpecField(source='link',
                          processors=[],
                          format='PNG',
                          options={'quality': 60})
    thumbnail = ImageSpecField(source='link',
                               processors=[ResizeToFill(270, 372)],
                               format='PNG',
                               options={'quality': 60})
    paging = ImageSpecField(source='link',
                            processors=[ResizeToFill(147, 143)],
                            format='PNG',
                            options={'quality': 60})
    is_delete = models.BooleanField(default=False, blank=True)


class VariantImage(models.Model):
    product = models.ForeignKey(ProductVariant, on_delete=models.DO_NOTHING, db_index=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    ink = models.ImageField(upload_to=upload_to)
    full = ImageSpecField(source='link',
                          processors=[],
                          format='PNG',
                          options={'quality': 60})
    thumbnail = ImageSpecField(source='link',
                               processors=[ResizeToFill(270, 372)],
                               format='PNG',
                               options={'quality': 60})
    paging = ImageSpecField(source='link',
                            processors=[ResizeToFill(147, 143)],
                            format='PNG',
                            options={'quality': 60})
    is_delete = models.BooleanField(default=False, blank=True)


class Stock(models.Model):
    is_delete = models.BooleanField(default=False, blank=True)


class StockLocation(models.Model):
    is_delete = models.BooleanField(default=False, blank=True)


class ProductToCatalog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    catalog = models.ForeignKey("Catalog", on_delete=models.SET_NULL, null=True)
    is_delete = models.BooleanField(default=False, blank=True)


class AttributeForProduct(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    code = models.CharField(max_length=20, db_index=True)
    CAST_CHOICES = (
        ('str', 'Строка'),
        ('int', 'Целое число'),
        ('color', 'Цвет'),
        ('float', 'Дробное число'),
    )
    cast_type = models.CharField(max_length=10, choices=CAST_CHOICES)
    is_delete = models.BooleanField(default=False, blank=True)


class ProductAttributes(models.Model):
    attribute = models.ForeignKey(AttributeForProduct, on_delete=models.DO_NOTHING, default=None, null=True, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, default=None, null=True, db_index=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.DO_NOTHING, blank=True, default=None, null=True, db_index=True)
    value = models.CharField(max_length=300, default='n/a', blank=True)
    is_delete = models.BooleanField(default=False, blank=True)


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, db_index=True, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, db_index=True, null=True)

