import requests

# Your OpenWeather API key
api_key = "5b435835d1e4d5743e63d4693b94d6f0"

# Example URL of the OpenWeather API endpoint for 5-day weather forecast data
city = "Coimbatore"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"  # units=metric for Celsius

# Making a GET request to the API endpoint
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the response JSON
    data = response.json()

    # Extracting specific data from the JSON response
    forecasts = data['list']

    print(f"5-Day Weather Forecast for {city}:")

    for forecast in forecasts:
        # Extracting the date and time
        dt_txt = forecast['dt_txt']

        # Extracting temperature, feels like temperature
        temperature = forecast['main']['temp']  # Temperature in Celsius
        feels_like = forecast['main']['feels_like']  # Feels like temperature in Celsius

        # Extracting the minimum and maximum temperature
        temp_min = forecast['main']['temp_min']
        temp_max = forecast['main']['temp_max']

        # Extracting the humidity
        humidity = forecast['main']['humidity']  # Humidity in percentage

        # Extracting the pressure
        pressure = forecast['main']['pressure']  # Atmospheric pressure in hPa

        # Extracting the wind speed and direction
        wind_speed = forecast['wind']['speed']  # Wind speed in m/s
        wind_deg = forecast['wind']['deg']  # Wind direction in degrees

        # Extracting the weather description
        weather_description = forecast['weather'][0]['description']  # Weather description

        # Extracting cloudiness
        cloudiness = forecast['clouds']['all']  # Cloudiness in percentage

        # Extracting precipitation data (rain and snow)
        rain = forecast.get('rain', {}).get('3h', 0)  # Rain volume for the last 3 hours
        snow = forecast.get('snow', {}).get('3h', 0)  # Snow volume for the last 3 hours

        # Extracting visibility
        visibility = forecast.get('visibility', 0)  # Visibility in meters

        # Extracting sea level and ground level pressure
        sea_level = forecast['main'].get('sea_level', 'N/A')  # Sea level pressure in hPa
        grnd_level = forecast['main'].get('grnd_level', 'N/A')  # Ground level pressure in hPa

        print(f"Date & Time: {dt_txt}")
        print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
        print(f"Min Temperature: {temp_min}°C, Max Temperature: {temp_max}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind: {wind_speed} m/s at {wind_deg}°")
        print(f"Weather Description: {weather_description}")
        print(f"Cloudiness: {cloudiness}%")
        print(f"Rain: {rain} mm")
        print(f"Snow: {snow} mm")
        print(f"Visibility: {visibility} meters")
        print(f"Sea Level Pressure: {sea_level} hPa")
        print(f"Ground Level Pressure: {grnd_level} hPa")
        print("---")
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")
