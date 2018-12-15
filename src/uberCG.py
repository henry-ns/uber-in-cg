import time
import datetime as dt
import pandas as pd
import numpy as np

from uber_rides.session import Session
from uber_rides.client import UberRidesClient

UberToken = 'ClIxUNRKCkMdDcabwJVpx4H0Tum4ZwFOdVzj8qkQ'
ProductId = 'd19e0080-4039-4a6f-97de-d00e0f43f3cc'



session = Session(server_token=UberToken)
client = UberRidesClient(session)


while True:
    time_initial = dt.datetime.now()
    nbhoods_data = {}
    for bairro in Bairros:
        estimates = []
        for point in bairro['points']:
            response = client.get_pickup_time_estimates(     
                start_latitude=point['latitude'],
                start_longitude=point['longitude'],
                product_id=ProductId)
