from shop.models import Catalog, CatalogTag


class CatalogAdapter:

    @classmethod
    def get_catalog_nodes(cls):
        root_nodes = Catalog.objects.root_nodes()
        return root_nodes

    @classmethod
    def get_section_by_slug(cls, slug):
        section = Catalog.objects.get(code=slug)
        return section
