import requests

BASE_URL = "http://127.0.0.1:8000"


def get_uploads():
    response = requests.get(f"{BASE_URL}/uploads")
    response.raise_for_status()
    return response.json()


def upload_file(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type,
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files,
    )

    response.raise_for_status()

    return response.json()