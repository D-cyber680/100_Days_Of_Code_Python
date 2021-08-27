import requests
import datetime
parameters = {
    "lat" : 32.514946 ,
    "lng" : -117.038246,
    "formatted" : 0
}

response = requests.get('https://api.sunrise-sunset.org/json',params = parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.datetime.now()

print(time_now.hour)