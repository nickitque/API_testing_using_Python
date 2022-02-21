import requests

"""API URLS"""
url = "https://reqres.in/api/users/2"

response = requests.delete(url)

"""Fetch response code"""
print(f"The response code is {response.status_code}")
assert response.status_code == 204
assert response.status_code != 200