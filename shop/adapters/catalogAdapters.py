from shop.models import Catalog, CatalogTag


class CatalogAdapter:

    @classmethod
    def get_catalog_nodes(cls):
        root_nodes = Catalog.objects.root_nodes()
        return root_nodes

