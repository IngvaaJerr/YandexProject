import requests
import configuration
import data

#функция создания заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
#функция получения трека заказа из ответа создания заказа
def get_order_track():
    post_response = post_new_order(data.order_body)
    track = post_response.json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_GETTING_PATH, params = {"t": track})
