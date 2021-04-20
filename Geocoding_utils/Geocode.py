import json
import requests

import pandas as pd

from Geocoding_utils.config import *


def geocode(data_to_geocode,
            address_col_name=ADDRESS,
            postal_code_col_name=POSTAL_CODE,
            city_col_name=CITY):
    data_for_request = data_to_geocode[[postal_code_col_name, city_col_name, address_col_name]].fillna("")
    data_for_request.rename(columns={
        address_col_name: ADDRESS,
        postal_code_col_name: POSTAL_CODE,
        city_col_name: CITY
    }, inplace=True)
    request_data = data_for_request.to_dict('records')

    response = requests.post('http://localhost:8088/geocode_file', json=json.dumps(request_data))
    geocoded_data = pd.json_normalize(response.json()['data'])
    data_to_geocode['lon'], data_to_geocode['lat'] = geocoded_data['lon'], geocoded_data['lat']
    return data_to_geocode
