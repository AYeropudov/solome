class CatalogNotFound(Exception):
    def __init__(self, message='Not found', *args):
        Exception.__init__(self, message)


class CatalogSaveException(Exception):
    def __init__(self, message='Not found', *args):
        Exception.__init__(self, message)
