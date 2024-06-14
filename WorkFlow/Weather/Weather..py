from fastapi import FastAPI
import aiohttp
from datetime import datetime

app = FastAPI()

# Replace this with your actual OpenWeatherMap API key
API_KEY = "ca7bbdd9f1827d83ee9e8e2a235a0ed4"

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Dictionary to map wind direction degrees to cardinal directions
WIND_DIRECTIONS = {
    range(int(round(348.76)), 360): "N",
    range(0, int(round(11.25))): "N",
    range(int(round(11.25)), int(round(33.75))): "NNE",
    range(int(round(33.75)), int(round(56.25))): "NE",
    range(int(round(56.25)), int(round(78.75))): "ENE",
    range(int(round(78.75)), int(round(101.25))): "E",
    range(int(round(101.25)), int(round(123.75))): "ESE",
    range(int(round(123.75)), int(round(146.25))): "SE",
    range(int(round(146.25)), int(round(168.75))): "SSE",
    range(int(round(168.75)), int(round(191.25))): "S",
    range(int(round(191.25)), int(round(213.75))): "SSW",
    range(int(round(213.75)), int(round(236.25))): "SW",
    range(int(round(236.25)), int(round(258.75))): "WSW",
    range(int(round(258.75)), int(round(281.25))): "W",
    range(int(round(281.25)), int(round(303.75))): "WNW",
    range(int(round(303.75)), int(round(326.25))): "NW",
    range(int(round(326.25)), int(round(348.76))): "NNW",
}

async def fetch_weather_forecast(city: str, session: aiohttp.ClientSession):
    """
    Asynchronously retrieves the weather forecast for the next 7 days for the specified city using the OpenWeatherMap API.
    """
    query_params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use metric units for temperature
    }
    try:
        async with session.get(BASE_URL, params=query_params) as response:
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            data = await response.json()

            # Extract relevant information from the API response
            forecast = []
            for entry in data["list"]:
                date = datetime.fromtimestamp(entry["dt"]).strftime("%Y-%m-%d %H:%M:%S")
                temperature = entry["main"]["temp"]
                description = entry["weather"][0]["description"]
                humidity = entry["main"]["humidity"]
                wind_speed = entry["wind"]["speed"]
                wind_direction_degrees = entry["wind"]["deg"]
                wind_direction = get_cardinal_direction(wind_direction_degrees)
                temp_min = entry["main"]["temp_min"]
                temp_max = entry["main"]["temp_max"]
                pressure = entry["main"]["pressure"]
                cloudiness = entry["clouds"]["all"]
                ground_level_pressure = entry["main"].get("grnd_level", "N/A")

                forecast.append({
                    "date": date,
                    "temperature": temperature,
                    "description": description,
                    "humidity": humidity,
                    "wind_speed": wind_speed,
                    "wind_direction": wind_direction,
                    "temp_min": temp_min,
                    "temp_max": temp_max,
                    "pressure": pressure,
                    "cloudiness": cloudiness,
                    "ground_level_pressure": ground_level_pressure
                })

            return forecast
    except aiohttp.ClientError as e:
        return {"error": str(e)}

def get_cardinal_direction(degrees):
    """
    Returns the cardinal direction (N, NE, E, SE, S, SW, W, NW) based on the provided wind direction degrees.
    """
    for direction_range, cardinal_direction in WIND_DIRECTIONS.items():
        if degrees in direction_range:
            return cardinal_direction
    return "Unknown"

@app.get("/forecast/{city}")
async def get_weather_forecast(city: str):
    async with aiohttp.ClientSession() as session:
        forecast = await fetch_weather_forecast(city, session)
        return forecast

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)