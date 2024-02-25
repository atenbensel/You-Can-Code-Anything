import requests

def fetch_weather_forecast(api_key, city):
    """
    Fetch weather forecast for a given city using OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "Error fetching weather forecast. Please try again."

def main():
    print("Welcome to the Weather Forecast App!")
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the city name: ")

    weather_forecast = fetch_weather_forecast(api_key, city)
    print(weather_forecast)

if __name__ == "__main__":
    main()
