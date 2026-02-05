import requests

def test_api_status_code():
    RESPONSE_CODE_OK = 200
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert response.status_code == RESPONSE_CODE_OK

# Test PR Trigger
