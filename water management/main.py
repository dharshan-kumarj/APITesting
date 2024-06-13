from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
import httpx

app = FastAPI()

# Define the data model
class WaterData(BaseModel):
    location: str
    water_level: float
    water_quality: str
    last_updated: str

# Mock external API URL (replace with real API if available)
EXTERNAL_API_URL = "https://eaas.meersens.com/api/me"

# Your API key for the external API
API_KEY = ""

# Dependency to get the API key from the request header
def get_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Water Management API"}

@app.get("/water-data/{location}", response_model=WaterData, dependencies=[Depends(get_api_key)])
async def get_water_data(location: str):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = await client.get(f"{EXTERNAL_API_URL}?location={location}", headers=headers)
        if response.status_code == 200:
            data = response.json()
            return WaterData(
                location=data["location"],
                water_level=data["water_level"],
                water_quality=data["water_quality"],
                last_updated=data["last_updated"]
            )
        else:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data from external API")

@app.post("/water-data/", response_model=WaterData, dependencies=[Depends(get_api_key)])
async def create_water_data(water_data: WaterData):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = await client.post(EXTERNAL_API_URL, json=water_data.dict(), headers=headers)
        if response.status_code == 201:
            return water_data
        else:
            raise HTTPException(status_code=response.status_code, detail="Error posting data to external API")
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
