# Water Level API

This FastAPI application provides a simple API to fetch weather forecasts for a given city using the OpenWeatherMap API.

FastAPI provides automatic interactive API documentation. You can access this documentation by visiting:
   [http://localhost:8000/docs](http://localhost:8000/docs)

After starting the application, open this URL in your web browser to explore the API endpoints, test the API directly from the browser, and view detailed information about request/response models.

Alternatively, you can also access the ReDoc-styled documentation at:
[http://localhost:8000/redoc](http://localhost:8000/redoc)

These interactive documentation pages are automatically generated based on the OpenAPI (formerly known as Swagger) specifications of your FastAPI application. They provide a user-friendly interface to understand and test your API without any additional setup.

For more information on FastAPI's automatic documentation features, you can visit the [official FastAPI documentation](https://fastapi.tiangolo.com/features/#automatic-docs).

The Response Data are : 

- **Water Level (Temperature)**: 286.41 K
- **Lowest Value Point (Humidity)**: 91%
- **Potential Action Point (Pressure)**: 1002 hPa

  ```json
  {
      "water_level": 286.41,
      "lowest_value_point": 91,
      "potential_action_point": 1002
  }

This data provides information about the weather conditions at the specified location. The water level represents the temperature in Kelvin, the lowest value point indicates humidity as a percentage, and the potential action point represents atmospheric pressure in hectopascals (hPa).
