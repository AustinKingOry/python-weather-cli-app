import requests
import argparse

API_KEY = '7169fa020d30957abbc8d193d4a893cb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather: {weather['description']}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("City not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the current weather information for a city.")
    parser.add_argument("city", type=str, help="Name of the city")
    
    args = parser.parse_args()
    get_weather(args.city)
