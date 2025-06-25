import requests
from configuration import CREATE_ORDER_URL, GET_ORDER_BY_TRACK_URL
from data import HEADERS, ORDER_DATA

def create_order():
    response = requests.post(
        CREATE_ORDER_URL,
        json=ORDER_DATA,
        headers=HEADERS
    )
    response.raise_for_status()
    return response.json()["track"]

def get_order_by_track(track_number):
    return requests.get(
        GET_ORDER_BY_TRACK_URL,
        params={'t': track_number},
        headers=HEADERS
    )