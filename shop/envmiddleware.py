import os
from django.shortcuts import redirect
from django.urls import reverse


class EnvMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if os.environ.get('DJANGO_MAINTENANCE') is '1' and not request.META['HTTP_HOST'].startswith('dev'):
            if request.META['PATH_INFO'] != '/maintenance':
                return redirect(reverse('maintenance'))

        return self.get_response(request)
