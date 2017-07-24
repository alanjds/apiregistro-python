===========
Basic Usage
===========


Client creation
===============

    >>> import apiregistro
    >>> client = apiregistro.Client(token='9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b')


Finding a domain
================

Anyone can find domains

    >>> client.domain_search('mysite.com.br')
    >>> client.domain_search('myavailablesite.com.br')
    [{u'available': True, u'status': u'available', u'price': ...cli, u'full_domain': u'myavailablesite.com.br'}]

And get its details

    >>> client.domain_info('myavailablesite.com.br')
    {u'available': True, u'status': u'available', u'price': u'40.00', u'full_domain': u'myavailablesite.com.br'}


Contact management
==================

An account should have at least one Contact being managed to be able to buy a domain

    >>> client.contact_list()
    []

Creation of Contacts can fail, mostly if it already exists or if
its document does not pass on validation checks

    >>> answer = client.contact_create(name="Impossible_Named_Person", document="123123123XY", email="impossible@namedperson.com")
    >>> answer[0]
    (True, ..., <Response [400]>)

    >>> answer = client.contact_create(name="Joey Ramone", document="26463464686", email="joey@ramone.com")
    >>> answer[0]
    (True, ..., <Response [201]>)

Providing a document, details of the owning contact are presented,
if this document does have a contact.

    >>> answer = client.contact_info(document="123123123XY")
    >>> answer
    (False, ..., <Response [404]>)

Buying a domain
===============

But to buy, a 'document' is usually needed.

    >>> answer = client.domain_buy('myavailablesite.com.br')
    >>> answer[0]
    (False, ..., <Response [400]>)

And the 'document' should belong to an existent Contact manageable by you.

    >>> answer = client.domain_buy('myavailablesite.com.br', document='26463464686')
    >>> answer[0]
    (True, ..., <Response [200]>)

.. testsetup:

    >>> 'spam'
    'spam'
