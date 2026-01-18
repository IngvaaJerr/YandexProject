import data
import post_and_get_requests

def test_track_search():
    post_response = post_and_get_requests.post_new_order(data.order_body)
    get_response = post_and_get_requests.get_order_track()
    assert get_response.status_code == 200