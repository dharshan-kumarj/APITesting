from fastapi import FastAPI, HTTPException
import httpx
import logging

app = FastAPI()

AGROMONITORING_API_URL = "https://home.agromonitoring.com/users/api-keys"
API_KEY = "cc20278f65b2088de2dc1af20fabbe06"  # Replace with your actual API key

logging.basicConfig(level=logging.INFO)

@app.get("/soil_data/")
async def get_soil_data(lat: float, lon: float):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "lat": lat,
        "lon": lon
    }

    async with httpx.AsyncClient() as client:
        try:
            logging.info(f"Sending request to {AGROMONITORING_API_URL} with params: {params}")
            response = await client.get(
                AGROMONITORING_API_URL,
                params=params,
                headers=headers
            )
            response.raise_for_status()
            logging.info(f"Received response: {response.text}")
        except httpx.HTTPStatusError as exc:
            logging.error(f"HTTP error occurred: {exc}")
            raise HTTPException(status_code=exc.response.status_code, detail=str(exc))
        except Exception as exc:
            logging.error(f"Unexpected error occurred: {exc}")
            raise HTTPException(status_code=500, detail=str(exc))

        try:
            data = response.json()
            return data
        except ValueError as exc:
            logging.error(f"Error decoding JSON response: {exc}")
            raise HTTPException(status_code=500, detail="Error decoding response from API")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)