import requests

BASE_URL = "http://127.0.0.1:8000"


def get_uploads():
    response = requests.get(f"{BASE_URL}/uploads")
    return response.json()