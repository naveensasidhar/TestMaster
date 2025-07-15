# need to create a free profile in weatherapi.com and then only we can invoke the api call.

#copied the url after providing the location in the weatherapi.com site

# third party exports
import requests

# Request url
url ="http://api.weatherapi.com/v1/current.json?key=3dfc4a1300a24b33814223011251507&q=L3S0A5&aqi=no"

#response back
response = requests.get(url)
weather_json = response.json()

#print the details
print(weather_json)

#temp variable.
temp = weather_json.get("current").get("temp_c")
place = weather_json.get("location").get("name")
remarks = weather_json.get("current").get("condition").get("text")
print("Temperature For Location:", place)
print("Temperature In Degree Celcius:", temp)
print("Remarks For The Day:", remarks)

#now lets make the url more generic buy passing the city.
# lets try to get inout from user itself.
#city = 'munnar'
city = input("Enter The City For Weather Need To Be Checked:\n")
new_url = "http://api.weatherapi.com/v1/current.json?key=3dfc4a1300a24b33814223011251507&q=" + city + "&aqi=no"

print(new_url)

#response back
response = requests.get(new_url)
weather_json = response.json()

#print the details
print(weather_json)

#temp variable.
temp = weather_json.get("current").get("temp_c")
place = weather_json.get("location").get("name")
remarks = weather_json.get("current").get("condition").get("text")
print("Temperature For Location:", place)
print("Temperature In Degree Celcius:", temp)
print("Remarks For The Day:", remarks)