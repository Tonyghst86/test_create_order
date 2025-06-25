# Базовый URL API Яндекс Самокат
BASE_URL = "https://ed56a09c-e828-4fa1-93cf-1571e5736ac9.serverhub.praktikum-services.ru/api/v1"

# Эндпоинты API
CREATE_ORDER_URL = f"{BASE_URL}/orders"  # POST запрос для создания заказа
GET_ORDER_BY_TRACK_URL = f"{BASE_URL}/orders/track"  # GET запрос для получения заказа по треку