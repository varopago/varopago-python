# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from future.builtins import super
from future.builtins import range
from future.builtins import str

import time
import datetime
import os
import random
import re
import string
import sys
import unittest

from mock import patch, Mock

import varopago


def generate_order_id():

    order_id = 'oid-test-{0}-{1}'.format(
        random.randint(1, 3000), str(time.time())[7:])
    if len(order_id) > 20:
        order_id = order_id[:20]

    return order_id

NOW = datetime.datetime.now()

DUMMY_CARD = {
    'card_number': '4111111111111111',
    'holder_name': 'Juan Lopez',
    'expiration_month': NOW.month,
    'expiration_year': str(NOW.year + 4)[2:],
    "cvv2": "110",
    "address": {
        "line1": "Av. 5 de febrero No. 1080 int Roble 207",
        "line2": "Carrillo puerto",
        "line3": "Zona industrial carrillo puerto",
        "postal_code": "06500",
        "state": "Querétaro",
        "city": "Querétaro",
        "country_code": "MX"
    }
}

DUMMY_CHARGE = {
    'amount': 100,
    'card': DUMMY_CARD,
    'order_id': generate_order_id(),
    'method': 'card',
    'description': 'Dummy Charge',
}

DUMMY_CHARGE_STORE = {
    'amount': 100,
    'method': 'store',
    'description': 'Dummy Charge on Store',
}

DUMMY_PLAN = {
    'amount': 2000,
    'status_after_retry': 'cancelled',
    'name': 'Amazing Gold Plan',
    'retry_times': 2,
    'repeat_unit': 'month',
    'trial_days': 0,
    'repeat_every': 1,
    'id': ('varopago-test-gold-' +
           ''.join(random.choice(string.ascii_lowercase) for x in range(10)))
}

DUMMY_TRANSFER = {
    'amount': 400,
    'customer_id': 'acuqxruyv0hi1wfdwmym',
    'description': 'Dummy Transfer',
    'order_id': 'oid-00099',
}


class VaropagoTestCase(unittest.TestCase):
    RESTORE_ATTRIBUTES = ('api_version', 'api_key')

    def setUp(self):
        super(VaropagoTestCase, self).setUp()

        self._varopago_original_attributes = {}

        for attr in self.RESTORE_ATTRIBUTES:
            self._varopago_original_attributes[attr] = getattr(varopago, attr)

        api_base = os.environ.get('VAROPAGO_API_BASE')
        if api_base:
            varopago.api_base = api_base
        #Sandbox
        varopago.api_key = os.environ.get(
            'VAROPAGO_API_KEY', 'sk_10d37cc4da8e4ffd902cdf62e37abd1b')
        varopago.merchant_id = "mynvbjhtzxdyfewlzmdo"
        #Dev
        #varopago.api_key = os.environ.get(
        #    'VAROPAGO_API_KEY', '68df281c16184d47bb773d70abd4191b')
        #varopago.merchant_id = "m4se8bd4fef1mkzk6d1b"
        varopago.verify_ssl_certs = False

    def tearDown(self):
        super(VaropagoTestCase, self).tearDown()

        for attr in self.RESTORE_ATTRIBUTES:
            setattr(varopago, attr, self._varopago_original_attributes[attr])

    # Python < 2.7 compatibility
    def assertRaisesRegexp(self, exception, regexp, callable, *args, **kwargs):
        try:
            callable(*args, **kwargs)
        except exception as err:
            if regexp is None:
                return True

            if isinstance(regexp, str):
                regexp = re.compile(regexp)
            if not regexp.search(str(err)):
                raise self.failureException('"%s" does not match "%s"' %
                                            (regexp.pattern, str(err)))
        else:
            raise self.failureException(
                '%s was not raised' % (exception.__name__,))


class VaropagoUnitTestCase(VaropagoTestCase):
    REQUEST_LIBRARIES = ['urlfetch', 'requests', 'pycurl']

    if sys.version_info >= (3, 0):
        REQUEST_LIBRARIES.append('urllib.request')
    else:
        REQUEST_LIBRARIES.append('urllib2')

    def setUp(self):
        super(VaropagoUnitTestCase, self).setUp()

        self.request_patchers = {}
        self.request_mocks = {}
        for lib in self.REQUEST_LIBRARIES:
            patcher = patch("varopago.http_client.%s" % (lib,))

            self.request_mocks[lib] = patcher.start()
            self.request_patchers[lib] = patcher

    def tearDown(self):
        super(VaropagoUnitTestCase, self).tearDown()

        for patcher in list(self.request_patchers.values()):
            patcher.stop()


class VaropagoApiTestCase(VaropagoTestCase):

    def setUp(self):
        super(VaropagoApiTestCase, self).setUp()

        self.requestor_patcher = patch('varopago.api.APIClient')
        requestor_class_mock = self.requestor_patcher.start()
        self.requestor_mock = requestor_class_mock.return_value

    def tearDown(self):
        super(VaropagoApiTestCase, self).tearDown()

        self.requestor_patcher.stop()

    def mock_response(self, res):
        self.requestor_mock.request = Mock(return_value=(res, 'reskey'))


class MyResource(varopago.resource.APIResource):
    pass


class MySingleton(varopago.resource.SingletonAPIResource):
    pass


class MyListable(varopago.resource.ListableAPIResource):
    pass


class MyCreatable(varopago.resource.CreateableAPIResource):
    pass


class MyUpdateable(varopago.resource.UpdateableAPIResource):
    pass


class MyDeletable(varopago.resource.DeletableAPIResource):
    pass


class MyComposite(varopago.resource.ListableAPIResource,
                  varopago.resource.CreateableAPIResource,
                  varopago.resource.UpdateableAPIResource,
                  varopago.resource.DeletableAPIResource):
    pass
