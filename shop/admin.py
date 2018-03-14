from django.contrib import admin

# Register your models here.
from shop.models import Product, ProductAttributes, ProductClass, ProductImage, ProductVariant, AttributeForProduct, VariantImage
from shop.models import Tag, CatalogTag, Catalog, ProductTag, CatalogImage
from imagekit.admin import AdminThumbnail


admin.site.register(Product)
admin.site.register(ProductClass)
admin.site.register(ProductVariant)


@admin.register(ProductImage)
class AdminProductimage(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')

@admin.register(CatalogImage)
class AdminCatalogImage(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')


admin.site.register(ProductAttributes)
admin.site.register(AttributeForProduct)
admin.site.register(VariantImage)
admin.site.register(Catalog)

admin.site.register(Tag)
admin.site.register(CatalogTag)
admin.site.register(ProductTag)



