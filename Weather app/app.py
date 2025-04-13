import requests
import pyfiglet
from simple_chalk import chalk


#API Key for openWeatherMap
API_KEY = '72ad1ee2c4807e4b6539b71360a126b5'
#Base URL for openWeatherMap API
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

#Mapping of weather codes to weather icons
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}
country = input("Check the weather for a certain city: ") 

url = f"{BASE_URL}?q={country}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information."))
    exit()
data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Construct output with weather icon
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

# Print output
#print(chalk.green(output))

print(chalk.green.bold.underline(output))


