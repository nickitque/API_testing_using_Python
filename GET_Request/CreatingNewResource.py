"""Creating new resource on server using post method."""

import requests
import json

"""API URL"""
url = "https://reqres.in/api/users"

"""Read Input Json file"""
file = open('CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)