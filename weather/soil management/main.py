from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

SOILGRIDS_API_URL = "https://rest.isric.org/soilgrids/v2.0/properties/query"

@app.get("/soil_data/")
async def get_soil_data(lat: float, lon: float):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(SOILGRIDS_API_URL, params={"lon": lon, "lat": lat})
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=str(exc))
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

        data = response.json()
        return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)  # Change port if necessary
