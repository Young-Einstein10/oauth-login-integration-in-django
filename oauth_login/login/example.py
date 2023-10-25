import requests
import json


oauth_server_url = "http://localhost:8000"

# Replace the credentials below with your own

client_id = "qai64WhMT2YtEpS4gfXcfhGCuim9u22wvhTZdu0c"  # client ID from my app
client_secret = "NfO2QcdVlB6xCPLwdsmu5FojfpK3GKtLGlEwazo2yEJlgPfxQHTK26xGtTBUiPkZ3iLioFtzQf0JAPaLjy9e2dk0h96KIF4AXkvfolUbwa7Rm7BzeIxR5J904sakGvXj"  # client secret from my app
username = "admin"  # my user
password = "Ploik90*"  # user's password


# Function to obtain an OAuth token
def get_access_token():
    token_url = f"{oauth_server_url}/oauth/token/"
    data = {"grant_type": "password", "username": username, "password": password}
    auth = (client_id, client_secret)

    response = requests.post(token_url, data=data, auth=auth)

    if response.status_code == 200:
        access_token = response.json().get("access_token")
        return access_token
    else:
        print(f"Failed to obtain access token. Status code: {response.status_code}")
        print(response.text)
        return None


# Function to make an authenticated API request
def make_authenticated_api_request(access_token):
    api_url = f"{oauth_server_url}/api/users/"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to make the API request. Status code: {response.status_code}")
        print(response.text)
        return None


# Obtain an OAuth token
access_token = get_access_token()

if access_token:
    # Make an authenticated API request
    api_response = make_authenticated_api_request(access_token)
if api_response:
    print("API Response:")
    print(json.dumps(api_response, indent=4))
