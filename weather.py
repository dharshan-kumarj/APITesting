from fastapi import FastAPI
import aiohttp
from datetime import datetime

app = FastAPI()

# Replace this with your actual OpenWeatherMap API key
API_KEY = "ca7bbdd9f1827d83ee9e8e2a235a0ed4"

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

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

                forecast.append({
                    "date": date,
                    "temperature": temperature,
                    "description": description,
                    "humidity": humidity,
                    "wind_speed": wind_speed
                })

            return forecast

    except aiohttp.ClientError as e:
        return {"error": str(e)}

@app.get("/forecast/{city}")
async def get_weather_forecast(city: str):
    async with aiohttp.ClientSession() as session:
        forecast = await fetch_weather_forecast(city, session)
        return forecast

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)