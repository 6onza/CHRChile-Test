import requests

API_BIKES_URL = 'http://api.citybik.es/v2/networks/bikesantiago'

def get_bike_data():
    url = API_BIKES_URL
    try:
        response = requests.get(url)
        
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    
    except requests.exceptions.RequestException as err:
        print(f'Other error occurred: {err}')
    
    if response.status_code == 200:
            return response.json()
    else:
        return None