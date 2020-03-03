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

print "customer: ", customer

bank_account = customer.bank_accounts.all().data[0] # We get the first account

print "bank_account ", bank_account

payout = customer.payouts.create(method='bank_account', destination_id=bank_account.id, amount="100", description="First payout")

print "payout ", payout
payoutDeleted = varopago.Payout.delete_as_customer(customer.id, payout.id)
print "payoutDeleted: ", payoutDeleted

print "Creating payout as merchant"
payout = varopago.Payout.create_as_merchant(method="bank_account", destination_id=bank_account.id, amount=200.00, description="Payout")
print payout

print "Deleting payout as merchant ---------------->"
payoutDeleted = varopago.Payout.delete_as_merchant(payout.id)
print payoutDeleted


