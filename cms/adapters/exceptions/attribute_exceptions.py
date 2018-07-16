class AttributeSaveException(Exception):
    def __init__(self, message = 'Validation error', errors=None, *args):
        Exception.__init__(self, message)
        self.errors = errors


class AttributeNotFoundException(Exception):
    def __init__(self, message='Validation error', *args):
        Exception.__init__(self, message)
