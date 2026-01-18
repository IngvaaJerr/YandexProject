import data
import post_and_get_requests

#автотест проверки, включающий в себя создание заказа и запрос информации о нём по track, 
# а также проверка статуса
def test_track_search():
    post_response = post_and_get_requests.post_new_order(data.order_body)
    get_response = post_and_get_requests.get_order_track()
    assert get_response.status_code == 200
# Герр Игорь, 39-я когорта — Финальный проект. Инженер по тестированию плюс