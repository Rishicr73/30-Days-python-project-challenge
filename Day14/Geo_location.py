import requests

name = input("Enter city name :").lower()

url = f"https://nominatim.openstreetmap.org/search?q={name}&format=json&limit=1&addressdetails=1&extratags=1&namedetails="

response = requests.get(url)

if response.status_code == 200:
    response = response.json()
    #print(response)
    lat = round(float(response[0]['lat']),4)
    lon = round(float(response[0]['lon']),4)
    print(f"Latitude   : {str(lat) + '° N' if lat > 0 else str(abs(lat)) + '° S'}")
    print(f"Longitude  : {str(lon) + '° E' if lon > 0 else str(abs(lon)) + '° W'}")
    print(f"State      : {response[0]['address']['state']}")
    print(f"Country    : {response[0]['address']['country']}")
    
    
else:
    print("Not found !")   
