# Crop Information and Advisory API

This FastAPI application provides a simple API to fetch crop information and advisory data for a given crop using the MapMyCrop API.

FastAPI provides automatic interactive API documentation. You can access this documentation by visiting:

[http://localhost:8000/docs](http://localhost:8000/docs)

After starting the application, open this URL in your web browser to explore the API endpoints, test the API directly from the browser, and view detailed information about request/response models.

Alternatively, you can also access the ReDoc-styled documentation at:
[http://localhost:8000/redoc](http://localhost:8000/redoc)

These interactive documentation pages are automatically generated based on the OpenAPI (formerly known as Swagger) specifications of your FastAPI application. They provide a user-friendly interface to understand and test your API without any additional setup.

For more information on FastAPI's automatic documentation features, you can visit the [official FastAPI documentation](https://fastapi.tiangolo.com/features/#automatic-docs).

## API Endpoints

### GET /crop-info

This endpoint retrieves crop information and advisory data for a given crop.

#### Parameters

- `crop_name` (string, required): The name of the crop for which you want to fetch information and advisory data.

#### Response

The API will return a JSON object containing the following fields:

- `name` (string): The name of the crop.
- `description` (string): A description of the crop.
- `advisory` (string): Advisory information related to the crop, such as growing tips, pest management, or weather advisories.

#### Example Request
```bash
{
GET /crop-info?crop_name=wheat
}



#### Example Response

```json
{
  "name": "Wheat",
  "description": "Wheat is a cereal grain widely cultivated for its seed, a food staple used to produce flour for leavened bread, biscuits, pasta, and noodles.",
  "advisory": "Monitor for wheat rust and apply appropriate fungicides if necessary. Ensure proper irrigation and fertilization for optimal yields."
}
