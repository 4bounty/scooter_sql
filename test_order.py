#Денис Ромашкин 10я когорта, Дипломный проект. Инженер по тестированию плюс
import pytest
import requests
import configuration
import data

@pytest.fixture
def created_order():
    response = requests.post(configuration.BASE_URL + configuration.KITS_PATH, json=data.orders_body)
    assert response.status_code == 201
    response = response.json()
    return response.get("track")

def test_get_order_by_track(created_order):
        url = f'{configuration.BASE_URL}{configuration.RECEIVE_ORDER}{created_order}'
        response = requests.get(url)
        assert response.status_code == 200
