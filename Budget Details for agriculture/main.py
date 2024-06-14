from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

class AgricultureBudgetRequest(BaseModel):
    country_code: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Agriculture Budget API"}

@app.post("/agriculture_budget")
async def get_agriculture_budget(request: AgricultureBudgetRequest):
    country_code = request.country_code
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/AG.LND.AGRI.K2?format=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data from World Bank API")

    data = response.json()

    if not data or len(data) < 2:
        raise HTTPException(status_code=404, detail="No data found for the given country code")

    return data[1]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
