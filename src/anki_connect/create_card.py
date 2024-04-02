import requests
import json

# Define the URL for AnkiConnect
URL = "http://localhost:8765"


def create_card():
    payload = json.dumps(
        {
            "action": "addNote",
        }
    )


if __name__ == "__main__":
    create_card()
