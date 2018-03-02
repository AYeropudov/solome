from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Catalog(MPTTModel):
    title = models.CharField(max_length=300, db_index=True)
    code = models.SlugField(db_index=True)
    has_sub_cat = models.BooleanField(default=False, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.SET_NULL)
    is_delete = models.BooleanField(default=False, blank=True)

    class MPTTMeta:
        order_insertion_by = ['title']


class CatalogTag(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, db_index=True, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, db_index=True, null=True)