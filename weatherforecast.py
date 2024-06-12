from fastapi import FastAPI
import requests

app = FastAPI()

# Replace this with your actual OpenWeatherMap API key
API_KEY = "your_api_key_here"

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/forecast/{city}")
async def get_weather_forecast(city: str):
    """
    Retrieves the current weather forecast for the specified city using the OpenWeatherMap API.
    """
    query_params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use metric units for temperature
    }

    try:
        response = requests.get(BASE_URL, params=query_params)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()

        # Extract relevant information from the API response
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Run the server with: uvicorn main:app --reload
