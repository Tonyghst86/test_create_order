from sender_stand_request import create_order, get_order_by_track
# Антон иванов, 31-я когорта — Финальный проект. Инженер по тестированию плюс
def test_create_and_get_order():
    track = create_order()
    response = get_order_by_track(track)
    
    # Проверка статус-кода
    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
    
    # Проверка структуры ответа
    response_data = response.json()
    assert "order" in response_data, "Ключ 'order' отсутствует в ответе"
    
    order = response_data["order"]
    assert order["firstName"] == "Антон"
    assert order["comment"] == "Тестовый заказ"