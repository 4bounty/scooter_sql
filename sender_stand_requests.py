import configuration
import requests
import data

# Создание нового заказа
def create_order():
    return requests.post(configuration.BASE_URL + configuration.KITS_PATH, json=data.orders_body)

# Получение заказа по номеру
def get_orders_by_track(track):
    return requests.get(configuration.BASE_URL + configuration.RECEIVE_ORDER + str(track))
