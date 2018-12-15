import time
import datetime as dt
import pandas as pd

import json

from uber_rides.session import Session
from uber_rides.client import UberRidesClient

UberToken = 'token'
ProductId = 'd19e0080-4039-4a6f-97de-d00e0f43f3cc'

session = Session(server_token=UberToken)
client = UberRidesClient(session)

data = open('../res/geo.json')
points = json.load(data)

time = dt.datetime.now()
nbhoods_data = {}
for point in points:
    response = client.get_pickup_time_estimates(     
        start_latitude=point['lat'],
        start_longitude=point['lng'],
        product_id=ProductId)
    estimate = response.json.get('times')[0]['estimate']
    nbhoods_data[point['address']] = pd.Series([estimate], index=[time_before])
dataFrame = pd.DataFrame(nbhoods_data)
dataFrame.to_csv('bairros_estimativas.csv', mode='a', header=False)