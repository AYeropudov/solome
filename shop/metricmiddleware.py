from django.db.models import F
from django.utils.crypto import salted_hmac

from back.models import Metric, MetricTotals
from viaescort import settings


class MetricMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        if request.session.session_key is None:
            request.session.create()
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.user.is_anonymous and request.method == 'GET':
            _hash = salted_hmac(settings.SECRET_KEY, "{}:{}:{}".format(request.META['REMOTE_ADDR'], request.session.session_key, request.META['PATH_INFO']).strip('/')).hexdigest()
            if len(request.META['QUERY_STRING']) == 0:
                _url = salted_hmac(settings.SECRET_KEY, request.META['PATH_INFO'].strip('/')).hexdigest()
            else:
                _url = salted_hmac(settings.SECRET_KEY, "{}{}".format(request.META['PATH_INFO'].strip('/'), request.META["QUERY_STRING"])).hexdigest()
            metric, is_new = Metric.objects.get_or_create(hash_counter=_hash, hash_url=_url, defaults={"hash_counter" : _hash, "hash_url": _url})
            _counters, _new = MetricTotals.objects.get_or_create(pk=_url, defaults={"id":_url, "counter":1})
            if is_new and not _new:
                _counters.counter += 1
                _counters.save()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response