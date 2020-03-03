import sys
import datetime
from os import path, pardir
PROJECT_ROOT = path.dirname(path.abspath(__file__))
sys.path.append(path.join(PROJECT_ROOT, pardir))

import varopago
varopago.api_key = "sk_10d37cc4da8e4ffd902cdf62e37abd1b"
varopago.verify_ssl_certs = False
varopago.merchant_id = "mynvbjhtzxdyfewlzmdo"

charge = varopago.Charge.create(
    customer="atun9ze7n1dvsdraj3fw",
    method="bank_account",
    amount=100.00,
    description="Testing customer charges from python",
    order_id="casdcf",
    due_date="2015-08-01T00:50:00Z",
    metadata={
        "data1":"value1",
        "data2":"value2"
    }
)

print(charge)