import sender_stand_requests

# Запрос на создание нового заказа
def test_order_creation():
    res = sender_stand_requests.create_order()
    #извлекаю трек из json
    track_id = res.json()['track']
    #получаю информацию о заказе по треку
    response = sender_stand_requests.get_orders_by_track(track_id)
    #проверяю что статус 200
    assert response.status_code == 200
