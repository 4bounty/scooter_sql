#Денис Ромашкин 10я когорта, Дипломный проект
import pytest
import requests
import configuration
import data

# Фикстура для создания заказа
@pytest.fixture
def created_order():
    # Выполняем запрос на создание заказа
    response = requests.post(configuration.BASE_URL + configuration.KITS_PATH, json=data.orders_body)
    # Проверяем успешность запроса на создание заказа
    assert response.status_code == 201
    # Извлекаем номер заказа (track) из ответа JSON и возвращаем его
    return response.json().get('track')

def test_get_order_by_track(created_order):
    # Выполняем запрос на получение заказа по треку заказа
    url = f'{configuration.BASE_URL}{configuration.RECEIVE_ORDER}{created_order}'
    response = requests.get(url)
    # Проверяем, что код ответа равен 200
    assert response.status_code == 200