class TagSaveException(Exception):
    def __init__(self, message = 'Validation error', errors=None, *args):
        Exception.__init__(self, message)
        self.errors = errors


class TagNotFoundException(Exception):
    def __init__(self, message='Not found', *args):
        Exception.__init__(self, message)
