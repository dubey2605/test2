import requests

# Example API URL
api_url = 'https://haigeniemwprod.eastus.cloudapp.azure.com:9998/api/endpoint_for_tables'

# If API requires authentication
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Content-Type': 'application/json'
}

# Making a GET request to fetch data
response = requests.get(api_url, headers=headers)

# Check status code for success
if response.status_code == 200:
    # Assuming the response contains JSON data
    data = response.json()
    print(data)
else:
    print('Failed to retrieve data:', response.status_code)


