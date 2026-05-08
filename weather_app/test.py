import requests



url = "http://api.openweathermap.org/geo/1.0/direct?q=Manila&limit=1&appid=bda1a8da7e08bd248eb9780e9bf46199"
response = requests.get(url)

lat = response.json()[0]['lat']
lon = response.json()[0]['lon']

url2 = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=bda1a8da7e08bd248eb9780e9bf46199&units=metric"
response = requests.get(url2)
print(response.json())
