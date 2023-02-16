import requests

API_BIKES_URL = 'http://api.citybik.es/v2/networks/bikesantiago'

def get_bike_data():
    url = API_BIKES_URL
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None