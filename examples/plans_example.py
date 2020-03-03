# -*- coding: utf-8 -*-
import sys
from os import path, pardir
PROJECT_ROOT = path.dirname(path.abspath(__file__))
sys.path.append(path.join(PROJECT_ROOT, pardir))

import varopago
varopago.api_key = "sk_10d37cc4da8e4ffd902cdf62e37abd1b"
varopago.verify_ssl_certs = False
varopago.merchant_id = "mynvbjhtzxdyfewlzmdo"
# Creating a plan
#plan = varopago.Plan.create(amount=150.00, status_after_retry="cancelled", retry_times=2,
#                           name="Curso de Ingles", repeat_unit="month", trial_days=30, repeat_every=1)
#print plan

# print "Updating plan with ID: pbkliysxavp8bvvp8f0k"
# plan = varopago.Plan.retrieve('pbkliysxavp8bvvp8f0k')
# plan.name="Curso de Ingles II"
# plan.save()
# print "All Plans"
# plans = varopago.Plan.all()
# print plans

print("Getting customer")
customer = varopago.Customer.retrieve('ancgmuvdtcvppcsfi3j4')
# print customer.cards.create(
# 	card_number="4111111111111111",
# 	holder_name="Juan Perez Ramirez",
# 	expiration_year="20",
# 	expiration_month="12",
# 	cvv2="110",
# 	address={
# 		"city":"Querétaro",
# 		"country_code":"MX",
# 		"postal_code":"76900",
# 		"line1":"Av 5 de Febrero",
# 		"line2":"Roble 207",
# 		"line3":"col carrillo",
# 		"state":"Queretaro"
#    })
print "Adding plan to user {0}".format(customer.name)
print('Getting subscription')
subscription = customer.subscriptions.retrieve("stxqkgt48ttknauk0xjx")

subscription.trial_end_date = "2019-01-11"
subscription.card = None
subscription.source_id = "kmfgttah2vdiyhow5x7r"

print('Updating subscription')
subscription.save()