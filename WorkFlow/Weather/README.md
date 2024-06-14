# Weather Forecast API

This FastAPI application provides a simple API to fetch weather forecasts for a given city using the OpenWeatherMap API.

FastAPI provides automatic interactive API documentation. You can access this documentation by visiting:
   [http://localhost:8000/docs](http://localhost:8000/docs)

After starting the application, open this URL in your web browser to explore the API endpoints, test the API directly from the browser, and view detailed information about request/response models.

Alternatively, you can also access the ReDoc-styled documentation at:
[http://localhost:8000/redoc](http://localhost:8000/redoc)

These interactive documentation pages are automatically generated based on the OpenAPI (formerly known as Swagger) specifications of your FastAPI application. They provide a user-friendly interface to understand and test your API without any additional setup.

For more information on FastAPI's automatic documentation features, you can visit the [official FastAPI documentation](https://fastapi.tiangolo.com/features/#automatic-docs).

This API returns weather forecast data for a given city. Below is an explanation of each field in the response:

- **date**: The date and time of the weather forecast.
- **temperature**: The current temperature in Celsius.
- **description**: A brief description of the weather conditions.
- **humidity**: The relative humidity percentage.
- **wind_speed**: The wind speed in meters per second.
- **wind_direction**: The direction of the wind.
- **temp_min**: The minimum temperature expected for the day in Celsius.
- **temp_max**: The maximum temperature expected for the day in Celsius.
- **pressure**: The atmospheric pressure in hPa (hectopascal).
- **cloudiness**: The percentage of cloud coverage.
- **ground_level_pressure**: The atmospheric pressure at ground level in hPa.

This JSON response provides weather forecast data for a specific date and time:

- **Date**: The date and time of the weather forecast. For this response, it is June 14, 2024, at 14:30.
- **Temperature**: The current temperature at the given date and time. In this case, it is 31.6°C.
- **Description**: Describes the weather conditions. Here, it is "overcast clouds", indicating the sky is covered by clouds.
- **Humidity**: Indicates the relative humidity at the time of the forecast. It is 47%, representing the amount of moisture in the air.
- **Wind Speed**: Specifies the speed at which the air is moving. It is 7.46 meters per second.
- **Wind Direction**: Indicates the direction from which the wind is blowing. In this case, it is "WSW" which stands for West-Southwest.
- **Min Temperature**: The minimum temperature expected for the day. It is 31.6°C.
- **Max Temperature**: The maximum temperature expected for the day. It is 32.59°C.
- **Pressure**: Represents the atmospheric pressure at the time of the forecast. It is 1008 hPa (hectopascal), a measure of the weight of the air above.
- **Cloudiness**: Indicates the percentage of cloud coverage. Here, the sky is covered by clouds up to 98%.
- **Ground Level Pressure**: Specifies the atmospheric pressure at ground level. It is 964 hPa.

This data provides a comprehensive overview of the weather conditions at the specified date and time.

Sample Response:
```json
{
    "date": "2024-06-14 14:30:00",
    "temperature": 31.6,
    "description": "overcast clouds",
    "humidity": 47,
    "wind_speed": 7.46,
    "wind_direction": "WSW",
    "temp_min": 31.6,
    "temp_max": 32.59,
    "pressure": 1008,
    "cloudiness": 98,
    "ground_level_pressure": 964
}

