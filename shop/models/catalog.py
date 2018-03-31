import uuid

from django.db import models
from imagekit.models import ImageSpecField
from mptt.models import MPTTModel, TreeForeignKey
from pilkit.processors import ResizeToFit, ResizeToCover, ResizeToFill


def upload_to(instance, filename):
    filename = str(uuid.uuid1()) + "." + filename.split('.', 1)[-1]
    return 'catalog/{}/{}'.format(instance.catalog.pk, filename)


class Catalog(MPTTModel):
    title = models.CharField(max_length=300, db_index=True)
    code = models.SlugField(db_index=True)
    has_sub_cat = models.BooleanField(default=False, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.SET_NULL)
    is_delete = models.BooleanField(default=False, blank=True)
    sort_position = models.SmallIntegerField(default=0, blank=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        if self.parent:
            return "{} - {}".format(self.parent.title, self.title)
        return self.title

    class Meta:
        verbose_name = 'Товарная Категория'
        verbose_name_plural = 'Товарные Категории'
        ordering = ['sort_position']


class CatalogTag(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, db_index=True, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, db_index=True, null=True)


class CatalogImage(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    link = models.ImageField(upload_to=upload_to)
    full = ImageSpecField(source='link',
                          processors=[],
                          format='PNG',
                          options={'quality': 60})
    thumbnail = ImageSpecField(source='link',
                               processors=[ResizeToFill(width=370, height=370)],
                               format='PNG',
                               options={'quality': 60})

    editor = ImageSpecField(source='link',
                            processors=[ResizeToFill(width=100, height=100)],
                            format='PNG',
                            options={'quality': 60})

    is_delete = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.catalog.title

    class Meta:
        verbose_name = 'Изображение каталога'
        verbose_name_plural = 'Изображения разделов каталога'
