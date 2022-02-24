"""Creating new resource on server using post method."""
import jsonpath
import requests
import json

"""API URL"""
url = "https://reqres.in/api/users/2"

"""Read Input Json file."""
file = open('CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

"""Make PUT request with Json Input body."""
response = requests.put(url, request_json)
print(response.content)

"""Validating response code."""
assert response.status_code == 200
assert response.status_code != 404

"""Parse response content"""
response_json = json.loads(response.text)
updated = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated[0])