import requests 
import passwords  # Importing username and password from passwords.py

# URL for authentication
url = f"http://localhost:8080/basic-auth/{passwords.USERNAME}/{passwords.PASSWORD}"

# Send request with authentication
response = requests.get(url, auth=(passwords.USERNAME, passwords.PASSWORD))

# Print response
print("Status Code:", response.status_code)
print("Response JSON:", response.json() if response.status_code == 200 else "Unauthorized")


