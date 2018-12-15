import datetime as dt
import json
import time

import pandas as pd

from uber_rides.session import Session
from uber_rides.client import UberRidesClient

uber_token = 'token'
product_id = 'd19e0080-4039-4a6f-97de-d00e0f43f3cc'

session = Session(server_token=uber_token)
client = UberRidesClient(session)

data = open('../res/geo.json')
points = json.load(data)

time = dt.datetime.now()
nbhoods_data = {}
for point in points:
    response = client.get_pickup_time_estimates(
        start_latitude=point['lat'],
        start_longitude=point['lng'],
        product_id=product_id
    )

    estimate = response.json.get('times')[0]['estimate']
    nbhoods_data[point['address']] = pd.Series([estimate], index=[time])

dataFrame = pd.DataFrame(nbhoods_data)
dataFrame.to_csv('bairros_estimativas.csv', mode='a', header=False)
