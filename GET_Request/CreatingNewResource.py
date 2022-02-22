"""Creating new resource on server using post method."""
import jsonpath
import requests
import json

"""API URL"""
url = "https://reqres.in/api/users"

"""Read Input Json file."""
file = open('CreateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

"""Make post request with Json Input body."""
response = requests.post(url, request_json)
print(response.content)

"""Validating response code."""
assert response.status_code == 201
assert response.status_code != 204

"""Fetch header from response."""
print(response.headers.get("Content-Length"))

"""Parse response to Json format."""
response_json = json.loads(response.text)

"""Pick id using Json path."""
id = jsonpath.jsonpath(response_json, "id")
print(id[0])
