from django.db import transaction
from django.db import IntegrityError
from cms.adapters.exceptions import TagNotFoundException, TagSaveException
from shop.models import Tag
from cms.forms import FormTag


class AdapterTags:
    @classmethod
    def create(cls, post_data):
        to_save = FormTag(post_data)
        if to_save.is_valid():
            try:
                to_save.full_clean()
                to_save.save()
            except IntegrityError:
                raise AttributeError()

    @classmethod
    def update(cls, attribute,  post_data):
        try:
            _instance = Tag.objects.get(pk=attribute)
            to_save = FormTag(post_data, instance=_instance)
            if to_save.is_valid():
                try:
                    to_save.full_clean()
                    to_save.save()
                except IntegrityError as e:
                    raise TagSaveException(str(e))
            else:
                raise TagSaveException(errors=to_save.errors)

        except Tag.DoesNotExist:
            raise TagNotFoundException()
