# the code will invoke a http request and the request will return date to the same.
# the data is returned in json data and we need to fetch and parse the same.
# pip usage.
import requests

# request and pass the http address
response = requests.get("http://api.open-notify.org/astros.json")

#decode the json from response
json = response.json()

print(json)

print("People Currently In Space are:")
for person in json["people"]:
    print(person["name"])