import requests

# Your OpenWeather API key
api_key = "fa4f706105a3478dfdf1d950ee3b302b"

# Example URL of the OpenWeather API endpoint for current weather data
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Making a GET request to the API endpoint
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the response JSON
    data = response.json()
    
    # Extracting specific data from the JSON response
    # Assuming we are interested in the temperature, humidity, and pressure
    water_level = data.get('main').get('temp')  # OpenWeather doesn't provide water level, using temperature as an example
    lvp = data.get('main').get('humidity')  # Using humidity as an example of Lowest Value Point
    pap = data.get('main').get('pressure')  # Using pressure as an example of Potential Action Point
    
    print(f"Water Level (Temperature): {water_level}K")
    print(f"Lowest Value Point (Humidity): {lvp}%")
    print(f"Potential Action Point (Pressure): {pap} hPa")
else:
    print(f"Failed to retrieve data: {response.status_code}")