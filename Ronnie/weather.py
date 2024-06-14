from fastapi import FastAPI
import httpx

app = FastAPI()

# Your OpenWeather API key
API_KEY = "5b435835d1e4d5743e63d4693b94d6f0"

# URL of the OpenWeather API endpoint for 5-day weather forecast data
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

@app.get("/weather/{city}")
async def get_weather_forecast(city: str):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        
        if response.status_code == 200:
            data = response.json()
            forecasts = data['list']
            forecast_data = []
            
            for forecast in forecasts:
                dt_txt = forecast['dt_txt']
                temperature = forecast['main']['temp']
                feels_like = forecast['main']['feels_like']
                temp_min = forecast['main']['temp_min']
                temp_max = forecast['main']['temp_max']
                humidity = forecast['main']['humidity']
                pressure = forecast['main']['pressure']
                wind_speed = forecast['wind']['speed']
                wind_deg = forecast['wind']['deg']
                weather_description = forecast['weather'][0]['description']
                cloudiness = forecast['clouds']['all']
                rain = forecast.get('rain', {}).get('3h', 0)
                snow = forecast.get('snow', {}).get('3h', 0)
                visibility = forecast.get('visibility', 0)
                sea_level = forecast['main'].get('sea_level', 'N/A')
                grnd_level = forecast['main'].get('grnd_level', 'N/A')
                
                forecast_data.append({
                    "date_time": dt_txt,
                    "temperature": temperature,
                    "feels_like": feels_like,
                    "temp_min": temp_min,
                    "temp_max": temp_max,
                    "humidity": humidity,
                    "pressure": pressure,
                    "wind_speed": wind_speed,
                    "wind_direction": wind_deg,
                    "weather_description": weather_description,
                    "cloudiness": cloudiness,
                    "rain": rain,
                    "snow": snow,
                    "visibility": visibility,
                    "sea_level_pressure": sea_level,
                    "ground_level_pressure": grnd_level
                })
            
            return {"city": city, "forecast": forecast_data}
        else:
            return {"error": f"Failed to retrieve data: {response.status_code} - {response.text}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)