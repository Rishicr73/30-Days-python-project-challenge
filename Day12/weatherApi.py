import requests
import json

city_name = input('City Name   : ').lower()

api_key = 'your api key' #Add your key here then only you can fetched the weather info of city.

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={'metric'}"

response = requests.get(url)  #to request data from the server.

if response.status_code == 200:        
    response = response.json()
    print(f"Description : {response['weather'][0]['description']}")
    print(f"Temperature : {response['main']['temp']} °C")
    print(f"Pressure    : {response['main']['pressure']} hPa")
    print(f"Humidity    : {response['main']['humidity']} %")
else:
    print('Page Not Found :(')
