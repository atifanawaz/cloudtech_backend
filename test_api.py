import requests

BASE_URL = "https://extraordinary-achievement-production.up.railway.app"

# Step 1: Test root endpoint
response = requests.get(f"{BASE_URL}/")
print("Root endpoint:", response.status_code, response.json())

# Step 2: Submit data
submit_data = {
    "username": "atif",
    "email": "atif@example.com",
    "data": "Test data"
}
response = requests.post(f"{BASE_URL}/api/submit", json=submit_data)
print("Submit data:", response.status_code, response.json())

# Step 3: Get all data
response = requests.get(f"{BASE_URL}/api/all")
print("All data:", response.status_code, response.json())
