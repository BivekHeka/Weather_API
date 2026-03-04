import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"



api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


weather_params = {
    "lat":27.677960,
    "lon":85.361461,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "It's going to rain today. Remember your an umbrella",
        from_ = "+19852562936",
        to = "+9779818035929"
    )
    print("SMS Status:", message.status)
print("Weather API Status:", response.status_code)