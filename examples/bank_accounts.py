# -*- coding: utf-8 -*-
import sys
from os import path, pardir
PROJECT_ROOT = path.dirname(path.abspath(__file__))
sys.path.append(path.join(PROJECT_ROOT, pardir))

import varopago
varopago.api_key = "sk_10d37cc4da8e4ffd902cdf62e37abd1b"
varopago.verify_ssl_certs = False
varopago.merchant_id = "mynvbjhtzxdyfewlzmdo"

customer = varopago.Customer.retrieve('amce5ycvwycfzyarjf8l')

print "Listing bank accounts for {0}".format(customer.name)
print customer.bank_accounts.all()

print "Creating account"
print customer.bank_accounts.create(clabe="646180109490000112", alias="Cuenta principal", holder_name="Carlos Alberto Aguilar")

print "Listing bank accounts for {0}".format(customer.name)
print customer.bank_accounts.all()
