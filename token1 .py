import requests
import os

# Set up the base URL and endpoint for API requests
base_url = "https://ec2-54-160-110-4.compute-1.amazonaws.com/"
token_endpoint = "/learn/api/public/v1/oauth2/token"

# Client credentials (store these securely; using environment variables is recommended)
client_id = 'd2005857-4fe4-4717-b223-f8636f1c8504'
client_secret = 'whdxgoh9BnY3MxPeOCN58rO0Bac6eRSy'

# Prepare the authentication header
auth = (client_id, client_secret) 

# Token request data
data = {
    'grant_type': 'client_credentials'
}

# Make a POST request to get the access token
response = requests.post(base_url + token_endpoint, auth=auth, data=data, verify=False)

# Check if the request was successful
if response.status_code == 200:
    token = response.json().get('access_token')
    print("Access Token:", token)
else:
    print("Failed to retrieve token:", response.status_code, response.text)

# You can now use the `token` to make further API requests







