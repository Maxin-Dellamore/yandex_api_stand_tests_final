import sender_stand_request
import data

def test_create_order_and_get_by_track():
    """Тест создания заказа и получения по треку"""
    
    # Шаг 1: Выполнить запрос на создание заказа
    order_response = sender_stand_request.post_new_order(data.order_body)
    
    # Проверяем, что заказ создался успешно
    assert order_response.status_code == 201, f"Ошибка создания заказа: {order_response.status_code}"
    
    # Шаг 2: Сохранить номер трека заказа
    track_number = order_response.json()['track']
    print(f"Создан заказ с треком: {track_number}")
    
    # Шаг 3: Выполнить запрос на получение заказа по треку
    track_response = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 4: Проверить, что код ответа равен 200
    assert track_response.status_code == 200, f"Ошибка получения заказа: {track_response.status_code}"
    
    # Дополнительные проверки (опционально)
    order_data = track_response.json()
    assert 'order' in order_data, "В ответе отсутствует объект 'order'"
    assert order_data['order']['track'] == track_number, "Трек в ответе не совпадает"
    
    print("Тест пройден успешно!")

# Запускаем тест
if __name__ == "__main__":
    test_create_order_and_get_by_track()
    