from urllib import response
import requests
API_KEY = "da3c8841b7fefd7de92e88c17cc55d2b"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name : \n")
response = requests.get(f"{API_URL}?appid={API_KEY}&q={city}")

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = int(data['main']['temp']-273.15)
    print(f"Weather info : {weather}")
    print(f"Temperature info : {temp} degree celsius")
else:
    print("No such city present in Database")
