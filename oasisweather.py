import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "conditions": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

def display_weather(weather):
    if weather:
        print(f"Weather report for {weather['location']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Conditions: {weather['conditions'].capitalize()}")
    else:
        print("Sorry, no weather data available for the specified location.")

def main():
    api_key = "40a46145d27964d96c181d41993a1c3d"
    location = input("Enter a city or ZIP code to get the current weather: ")
    weather = get_weather(api_key, location)
    display_weather(weather)

if __name__ == "__main__":
    main()