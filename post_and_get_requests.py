import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
def get_order_track():
    post_response = post_new_order(data.order_body)
    track = post_response.json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_GETTING_PATH, params = {"t": track})
