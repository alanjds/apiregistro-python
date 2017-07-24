# coding: utf-8
import logging
logger = logging.getLogger(__name__)

import slumber


class Client(object):
    def __init__(self, token=None, base_url='https://www.apiregistro.com.br:80', document=None):
        self.token = token
        self.document = document
        self._slumber = slumber.API(base_url + '/api/v1')
        self._slumber._store['session'].headers.update({
            'Token': token,
        })

    def __getattr__(self, name):
        return getattr(self._slumber, name)

    def domain_search(self, name):
        return self._slumber.domains.get(search=name)['results']

    def domain_info(self, name):
        return self._slumber.domains(name)

    def domain_buy(self, name, document=None):
        document = document or self.document
        if not document:
            raise RuntimeError("Cannot register a domain without a 'document'")

        result = self._slumber.domains(name).buy.post({
            'document': document,
        })
        return result
