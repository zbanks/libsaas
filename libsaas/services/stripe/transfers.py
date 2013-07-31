from libsaas.services import base
from libsaas import parsers, http

from . import resource


class TransfersBaseResource(resource.StripeResource):

    path = 'transfers'

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Transfer(TransfersBaseResource):
    pass


class Transfers(TransfersBaseResource):

    @base.apimethod
    def get(self, count=None, offset=None):
        """
        Fetch all of the objects.

        :var count: A limit on the number of objects to be returned.
            Count can range between 1 and 100 objects.
        :vartype count: int

        :var offset: An offset into your object array. The API will return
            the requested number of objects starting at that offset.
        :vartype offset: int
        """
        params = base.get_params(None, locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json
