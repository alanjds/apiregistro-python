# coding: utf-8
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
import six
from future.utils import python_2_unicode_compatible

import logging
logger = logging.getLogger(__name__)

import slumber


@python_2_unicode_compatible
class Client(object):
    def __init__(self, token=None, base_url='https://www.apiregistro.com.br:80', document=None):
        self._token = token
        self._document = document
        self._base_url = base_url
        self._slumber = slumber.API(base_url + '/api/v1')
        self._slumber._store['session'].headers.update({
            'Token': token,
        })

    def __repr__(self):
        try:
            u = six.text_type(self)
        except (UnicodeEncodeError, UnicodeDecodeError):
            u = '[Bad Unicode data]'
        return '<%s: %s>' % (self.__class__.__name__, u)

    def __str__(self):
        return 'token=%s base=%s document=%s' % (
            self._token,
            self._base_url,
            self._document,
        )

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
