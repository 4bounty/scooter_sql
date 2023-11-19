#Денис Ромашкин 10я когорта, Дипломный проект
import sender_stand_requests

# Запрос на создание нового заказа
def test_get_order_by_track():
    #Вызываю создание заказа
    new_response = sender_stand_requests.create_order()
    #Извлекаю трек из ответа созданного заказа
    track = new_response.json()['track']
    #ВВыполняем запрос на получение заказа по треку заказа
    response = sender_stand_requests.get_orders_by_track(track)
    #Проверем, что код ответа равен 200
    assert response.status_code == 200
