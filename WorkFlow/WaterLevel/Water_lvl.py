from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# Your OpenWeather API key
api_key = "fa4f706105a3478dfdf1d950ee3b302b"

@app.get("/weather/{city}")
async def get_weather(city: str):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            # Extracting specific data from the JSON response
            main_data = data.get('main', {})
            temperature = main_data.get('temp')  # Example: temperature as water level
            humidity = main_data.get('humidity')  # Example: humidity as lowest value point
            pressure = main_data.get('pressure')  # Example: pressure as potential action point
            
            return {
                "water_level": temperature,
                "lowest_value_point": humidity,
                "potential_action_point": pressure
            }
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to retrieve data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Water_lvl:app", host="0.0.0.0", port=8000, reload=True)

