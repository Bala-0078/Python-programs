import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
import json
import time
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(SCRIPT_DIR, "weather_cache.json")
CACHE_DURATION = 300 

ALL_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
    "Daman and Diu", "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep",
    "Puducherry"
]

class WeatherReport:
    def __init__(self, location_name, raw_data):
        self.location = location_name
        current = raw_data.get('current_weather', {})
        self.temp = current.get('temperature')
        self.wind_speed = current.get('windspeed')
    def __str__(self):
        return f"| {self.location:<30} | {self.temp:>5}°C | {self.wind_speed:>5} km/h |"

class WeatherClient:
    def __init__(self):
        self.weather_url = "https://api.open-meteo.com/v1/forecast"
        self.geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
        self.cache = self._load_cache()
    def _load_cache(self):
        if not os.path.exists(CACHE_FILE):
            return {}
        try:
            with open(CACHE_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    def _save_cache(self):
        try:
            with open(CACHE_FILE, 'w') as f:
                json.dump(self.cache, f, indent=4)
        except Exception as e:
            print(f"Error saving cache: {e}")
    def _get_coordinates(self, location_name):
        params = {"name": location_name, "count": 1, "language": "en", "format": "json"}
        try:
            response = requests.get(self.geocoding_url, params=params, verify=False)
            response.raise_for_status()
            data = response.json()
            if 'results' not in data or not data['results']:
                return None
            result = data['results'][0]
            return {
                "name": result['name'], 
                "lat": result['latitude'], 
                "lon": result['longitude']
            }
        except requests.RequestException:
            return None

    def get_weather(self, location_name):
        cache_key = location_name.title()
        current_time = time.time()
        if cache_key in self.cache:
            timestamp = self.cache[cache_key]['timestamp']
            if current_time - timestamp < CACHE_DURATION:
                return WeatherReport(self.cache[cache_key]['name'], self.cache[cache_key]['data'])
        coords = self._get_coordinates(location_name)
        if not coords:
            print(f"Could not find: {location_name}")
            return None
        params = {
            "latitude": coords['lat'], 
            "longitude": coords['lon'], 
            "current_weather": "true"
        }
        try:
            response = requests.get(self.weather_url, params=params, verify=False)
            response.raise_for_status()
            weather_data = response.json()
            self.cache[cache_key] = {
                "timestamp": current_time,
                "name": coords['name'],
                "data": weather_data
            }
            self._save_cache()
            return WeatherReport(coords['name'], weather_data)
        except requests.RequestException:
            print(f"Network Error for {location_name}")
            return None

def main():
    client = WeatherClient()
    print("\nfetching weather data for all Indian States...\n")
    print("-" * 60)
    print(f"| {'LOCATION':<30} | {'TEMP':>5}   | {'WIND':>10} |")
    print("-" * 60)
    for state in ALL_STATES:
        report = client.get_weather(state)
        if report:
            print(report)
        else:
            print(f"| {state:<30} |   N/A   |    N/A     |")
        time.sleep(1)
    print("-" * 60)
    print("Done.")

if __name__ == "__main__":
    main()