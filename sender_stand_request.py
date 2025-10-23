import configuration
import requests
import data

def post_new_order(body):
    """Создание нового заказа"""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body
    )

def get_order_by_track(track_number):
    """Получение заказа по треку"""
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track_number} 
    )

def get_new_order_track():
    """Получение трека заказа"""
    order_response = post_new_order(data.order_body)
    if order_response.status_code == 201:
        return order_response.json()['track'] 
    else:
        raise Exception(f"Ошибка создания заказа: {order_response.status_code}")
    