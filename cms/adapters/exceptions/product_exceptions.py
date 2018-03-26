class ProductException(Exception):
    def __init__(self,message, errors, *args):
        Exception.__init__(self, message)
        self.errors = errors
