import requests
from twilio.rest import Client

account_sid = "AC406022b11400b217efe615ab5b2a9dfa"
auth_token = "c9f28b4c51ee6ff852b8b1cab0839ef0"


api_key = "0a63ffd40ebe3b2da7b079eb5551d92f"
api_dict = {
    "lat" : 23.810331,
    "lon" : 90.412521,
    "exclude" : "current,minutely,daily",
    "appid" : api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=api_dict)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body='Hola yo del futuro! De : Daniel 🎨',
        from_='+17125269446',
        to='+526641258315'
    )

    print(message.status)

# weather_ids = []
# for i in range(0,13):
#     weather_ids.append(data["hourly"][i]["weather"][0]["id"])
#
# print(weather_ids)
# will_rain = False
# for ID in weather_ids:
#     if ID < 700:
#         will_rain = True
# if will_rain == True:
#     print("Bring an umbrella")
