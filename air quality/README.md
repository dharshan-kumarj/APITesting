# Air Quality API

This FastAPI application provides a simple API to fetch air quality data for a given location using the OpenWeatherMap API.

## Documentation

FastAPI provides automatic interactive API documentation. You can access this documentation by visiting:

- [http://localhost:8001/docs](http://localhost:8001/docs)

After starting the application, open this URL in your web browser to explore the API endpoints, test the API directly from the browser, and view detailed information about request/response models.

Alternatively, you can also access the ReDoc-styled documentation at:

- [http://localhost:8001/redoc](http://localhost:8001/redoc)

These interactive documentation pages are automatically generated based on the OpenAPI (formerly known as Swagger) specifications of your FastAPI application. They provide a user-friendly interface to understand and test your API without any additional setup.

For more information on FastAPI's automatic documentation features, you can visit the [official FastAPI documentation](https://fastapi.tiangolo.com/features/#automatic-docs).

## Response Data Explanation

The `/air_quality` endpoint returns the following response data:

### `location`

This object contains the latitude and longitude values that were passed as query parameters in the request. It acts as a reference for the location of the air quality data.

### `air_quality`

This object contains the actual air quality data retrieved from the OpenWeatherMap API.

- **coord**: This object contains the longitude and latitude coordinates of the location for which the air quality data is provided.
- **list**: This is an array containing one or more objects with air quality information. In this case, there is only one object in the array.
  - **main.aqi**: This is the Air Quality Index (AQI) value, which is a measure of air pollution. Higher values indicate higher levels of air pollution.
  - **components**: This object contains the concentrations of various air pollutants in micrograms per cubic meter (μg/m³):
    - **co**: Carbon monoxide concentration.
    - **no**: Nitrogen monoxide concentration.
    - **no2**: Nitrogen dioxide concentration.
    - **o3**: Ozone concentration.
    - **so2**: Sulfur dioxide concentration.
    - **pm2_5**: Particulate matter (PM2.5) concentration.
    - **pm10**: Particulate matter (PM10) concentration.
    - **nh3**: Ammonia concentration.
  - **dt**: This is the Unix timestamp (in seconds) for the time at which the air quality data was retrieved or measured.

In summary, the response data provides the location for which the air quality data is provided, the overall Air Quality Index (AQI) value, and the concentrations of various air pollutants. This information can be used to assess the air quality conditions at the specified location.
