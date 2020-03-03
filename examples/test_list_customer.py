import sys
import datetime
from os import path, pardir
from passlib.tests.utils import limit
PROJECT_ROOT = path.dirname(path.abspath(__file__))
sys.path.append(path.join(PROJECT_ROOT, pardir))

import varopago

varopago.api_key = "sk_10d37cc4da8e4ffd902cdf62e37abd1b"
varopago.verify_ssl_certs = False
varopago.merchant_id = "mynvbjhtzxdyfewlzmdo"

customers = varopago.Customer.all(
    external_id="AA_00002",
    limit=1
)

print(customers)
