import asyncio
import aiohttp
from fastapi import FastAPI

app = FastAPI()

# Define the API endpoint
@app.get("/crop-info")
async def get_crop_info(crop_name: str):
    # URL for the MapMyCrop API
    api_url = f"https://api.mapmycrop.com/api/v1/crops/{crop_name}"

    async with aiohttp.ClientSession() as session:
        try:
            # Make an asynchronous GET request to the API
            async with session.get(api_url) as response:
                response.raise_for_status()  # Raise an exception for non-2xx status codes
                data = await response.json()

                # Extract the relevant information from the API response
                crop_info = {
                    "name": data["name"],
                    "description": data["description"],
                    "advisory": data["advisory"],
                    # Add more fields as needed
                }

                return crop_info

        except aiohttp.ClientError as e:
            # Handle exceptions related to the API request
            return {"error": str(e)}

        except (KeyError, ValueError, TypeError):
            # Handle exceptions related to parsing the API response
            return {"error": "Invalid API response"}

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)