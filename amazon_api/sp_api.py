import os
import requests

# Retrieve your environment variables
client_id = os.getenv('AMAZON_CLIENT_ID')
client_secret = os.getenv('AMAZON_CLIENT_SECRET')
refresh_token = os.getenv('AMAZON_REFRESH_TOKEN')

def get_access_token():
    url = "https://api.amazon.com/auth/o2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
    }

    response = requests.post(url, headers=headers, data=data)

    # TODO: Add error handling here
    response_json = response.json()

    return response_json["access_token"]

# TODO: Add more functions here to make requests to different SP-API endpoints using the access token

