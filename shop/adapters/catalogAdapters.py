from shop.models import Catalog, CatalogTag
from shop.Exceprions import CatalogDoesNotExist


class CatalogAdapter:

    @classmethod
    def get_catalog_nodes(cls):
        root_nodes = Catalog.objects.root_nodes()
        return root_nodes

    @classmethod
    def get_section_by_slug(cls, slug):
        try:
            section = Catalog.objects.get(code=slug)
        except Catalog.DoesNotExist as ex:
            raise CatalogDoesNotExist()
        return section
