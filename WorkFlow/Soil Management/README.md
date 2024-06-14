# Soil Management API

This FastAPI application provides a simple API to fetch soil data for given coordinates using the Agromonitoring API.

## Interactive API Documentation

FastAPI provides automatic interactive API documentation. You can access this documentation by visiting:

[http://localhost:8001/docs](http://localhost:8001/docs)

After starting the application, open this URL in your web browser to explore the API endpoints, test the API directly from the browser, and view detailed information about request/response models.

Alternatively, you can also access the ReDoc-styled documentation at:
[http://localhost:8001/redoc](http://localhost:8001/redoc)

These interactive documentation pages are automatically generated based on the OpenAPI (formerly known as Swagger) specifications of your FastAPI application. They provide a user-friendly interface to understand and test your API without any additional setup.

# Soil Data Response Explanation

Let's break down each field in the response:

## 1. `"dt": 1718323200`
- This is a Unix timestamp, representing the date and time of the soil data measurement.
- The value 1718323200 corresponds to a date in the future (approximately July 13, 2024). 
- Note: This might be an example or placeholder value, as typically soil data would be for current or past dates.

## 2. `"t10": 301.253`
- This represents the soil temperature at 10 cm depth.
- The value is in Kelvin. To convert to Celsius, subtract 273.15.
- 301.253 K ≈ 28.103°C or about 82.585°F.

## 3. `"moisture": 0.106`
- This is the soil moisture.
- The value is typically represented as a fraction or percentage of water content in the soil.
- 0.106 suggests the soil moisture is about 10.6% or 0.106 m³/m³ (cubic meters of water per cubic meter of soil).

## 4. `"t0": 304.947`
- This likely represents the soil surface temperature (at 0 cm depth).
- Again, the value is in Kelvin.
- 304.947 K ≈ 31.797°C or about 89.235°F.

## Summary

This data provides information about the soil conditions at a specific time and location:
- The timestamp (which appears to be a future date, possibly for demonstration purposes)
- The temperature at 10 cm below the surface
- The soil moisture content
- The surface temperature

This kind of data is valuable for agricultural purposes, helping farmers and agronomists understand soil conditions for optimal crop management.

Sample Response:
```json
{
    "dt": 1718323200,
    "t10": 301.253,
    "moisture": 0.106,
    "t0": 304.947
}
