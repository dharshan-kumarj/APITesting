import requests

# Replace with your actual API keys
weatherbit_api_key = '64efca388d274fad847198f295f68b0c'
opencage_api_key = 'e2077ef4c9ee401ebaf345be209f68c0'

# Define the coordinates
latitude = 12.9716  # Example latitude
longitude = 77.5946  # Example longitude

# Construct the Weatherbit API URL
weatherbit_url = f'https://api.weatherbit.io/v2.0/current/airquality?lat={latitude}&lon={longitude}&key={weatherbit_api_key}'

# Make a request to the Weatherbit API
weatherbit_response = requests.get(weatherbit_url)

# Check if the request was successful
if weatherbit_response.status_code == 200:
    # Parse the JSON response
    air_quality_data = weatherbit_response.json()
    # Extract relevant air quality details
    air_quality = air_quality_data['data'][0]
    aqi = air_quality['aqi']
    pm10 = air_quality['pm10']
    pm25 = air_quality['pm25']
    o3 = air_quality['o3']
    no2 = air_quality['no2']
    so2 = air_quality['so2']
    co = air_quality['co']

    # Construct the Reverse Geocoding API URL
    reverse_geocoding_url = f'https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key={opencage_api_key}'

    # Make a request to the OpenCage Reverse Geocoding API
    reverse_geocoding_response = requests.get(reverse_geocoding_url)

    # Check if the request was successful
    if reverse_geocoding_response.status_code == 200:
        # Parse the JSON response
        reverse_geocoding_data = reverse_geocoding_response.json()
        if reverse_geocoding_data['results']:
            # Get the components of the first result
            components = reverse_geocoding_data['results'][0]['components']
            state = components.get('state', 'N/A')
            district = components.get('state_district', 'N/A')
            taluk = components.get('suburb', 'N/A')

            # Print the air quality details along with the location
            print(f"Location: {taluk}, {district}, {state}")
            print(f"Latitude: {latitude}, Longitude: {longitude}")
            print(f"Air Quality Index (AQI): {aqi}")
            print(f"PM10: {pm10} µg/m³")
            print(f"PM2.5: {pm25} µg/m³")
            print(f"O3: {o3} ppb")
            print(f"NO2: {no2} ppb")
            print(f"SO2: {so2} ppb")
            print(f"CO: {co} ppb")
        else:
            print("Error: No results found for the specified coordinates.")
    else:
        print(f"Error: Unable to fetch reverse geocoding data (Status code: {reverse_geocoding_response.status_code})")
else:
    print(f"Error: Unable to fetch air quality data (Status code: {weatherbit_response.status_code})")
