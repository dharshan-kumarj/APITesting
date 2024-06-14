from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

API_KEY = "22e9d54472dc3af790ba0aab12cd5781"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution"

@app.get("/air_quality")
async def get_air_quality(lat: float, lon: float):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "location": {"lat": lat, "lon": lon},
                "air_quality": data
            }
        else:
            raise HTTPException(status_code=response.status_code, detail="Error fetching air quality data")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)  # Change the port to 8001
