from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# Sample URL for agricultural bank schemes (replace with actual endpoint)
AGRI_SCHEMES_URL = "https://sbi.co.in/web/agri-rural"

@app.get("/agri-bank-schemes")
async def get_agri_bank_schemes():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(AGRI_SCHEMES_URL)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=500, detail=f"An error occurred while requesting data: {exc}")
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=f"Error response {exc.response.status_code} from {AGRI_SCHEMES_URL}: {exc.response.text}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
