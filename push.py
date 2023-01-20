import requests

from auth import secrets

webhook_url = secrets()[4]

def notify_push(content: str) -> None:
    payload = {"content": content}
    response = requests.post(webhook_url, data=payload)
    print(f"Discord webhook response: {response}")