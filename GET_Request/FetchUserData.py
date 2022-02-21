"""In this file I'm Fetching Data from the Json content."""

import requests
import json
import jsonpath

"""API URLS"""
url = "https://reqres.in/api/users?page=2"

"""Send Get Request """
response = requests.get(url)
print(response)

"""Display Response Content"""
# print(response.content)
# print(response.headers)

"""Parse response to Json format"""
json_response = json.loads(response.text)
print(json_response)

"""Fetch value using Json path"""
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(f"Total quantity of pages is {pages}")

"""Added asserts: positive and negative."""
assert pages == [2]
assert pages != [3]
