import requests

BASE_URL = "http://127.0.0.1:8000"


def get_uploads():
    try:
        response = requests.get(
            f"{BASE_URL}/uploads",
            timeout=5,
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:
        return []


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
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def process_invoice(upload_id):
    response = requests.post(
        f"{BASE_URL}/process/{upload_id}",
        timeout=60,
    )

    response.raise_for_status()

    return response.json()


def approve_invoice(upload_id):
    response = requests.post(
        f"{BASE_URL}/review/{upload_id}/approve",
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def reject_invoice(upload_id):
    response = requests.post(
        f"{BASE_URL}/review/{upload_id}/reject",
        timeout=30,
    )

    response.raise_for_status()

    return response.json()