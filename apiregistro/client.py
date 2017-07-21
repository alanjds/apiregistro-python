# coding: utf-8
import logging
logger = logging.getLogger(__name__)

class Client(object):
    def __init__(self, token):
        self.token = token
