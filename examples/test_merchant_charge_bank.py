import sys
import datetime
from os import path, pardir
PROJECT_ROOT = path.dirname(path.abspath(__file__))
sys.path.append(path.join(PROJECT_ROOT, pardir))

import varopago
varopago.api_key = "sk_10d37cc4da8e4ffd902cdf62e37abd1b"
varopago.verify_ssl_certs = False
varopago.merchant_id = "mynvbjhtzxdyfewlzmdo"

charge = varopago.Charge.create_as_merchant(
    method="bank_account",
    amount=100.00,
    description="Testing charges from python",
    order_id="casdcasdc",
    due_date="2015-08-01T00:50:00Z",
    customer={
        "name":"Gerry",
        "last_name":"Robles",
        "email":"gerry@example.com",
        "phone_number":"4429938834",
        "address":{
            "city": "Queretaro",
            "state":"Queretaro",
            "line1":"Calle de las penas no 10",
            "postal_code":"76000",
            "line2":"col. san pablo",
            "line3":"entre la calle de la alegria y la calle del llanto",
            "country_code":"MX"
        }
    },
    metadata={
        "data1":"value1",
        "data2":"value2"
    }
);

print(charge)