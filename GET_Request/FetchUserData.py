import requests


"""API URLS"""

url = "https://reqres.in/api/users?page=2"

"""Send Get Request """
response = requests.get(url)
print(response)

"""Display Response Content"""
print(response.content)