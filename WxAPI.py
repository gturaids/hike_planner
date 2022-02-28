import requests
import json
import time


# US Locations Only

def get_lat_long_from_zip(zip_code):
    """
    Takes a US zipcode as a parameter and returns a latitude and longitude.
    lat/long is required by the weather API used in the get_weather() function
    """
    with open("USCities.json", "r") as cities_file:
        cities_object = json.load(cities_file)
        for item in cities_object:
            if item['zip_code'] == zip_code:
                return item['latitude'], item['longitude']


def get_weather(zip_code):
    """
    Takes a US zipcode as a parameter and returns a string with the current weather at that location
    """
    lat, long = get_lat_long_from_zip(zip_code)

    # API entrypoint: generates metadata for the specified location
    # URL for location's weather is in the metadata
    meta_data = requests.get(f"https://api.weather.gov/points/{lat},{long}")

    with open('weather.json', 'wt') as data_file:
        data_file.write(meta_data.text)

    with open('weather.json', 'r') as data_file:
        meta_object = json.load(data_file)
        path_to_forecast = meta_object["properties"]["forecast"]

    # Retrieves weather from URL found in the metadata
    full_weather = requests.get(path_to_forecast)

    with open('weather.json', 'wt')as data_file:
        data_file.write(full_weather.text)

    with open('weather.json', 'r') as data_file:
        weather_object = json.load(data_file)
        detailed_forecast = weather_object["properties"]["periods"][0]["detailedForecast"]
        return detailed_forecast


#making this a microservice
# while True:
#     time.sleep(1)
#     print("Waiting for request.")
#     with open('weather.json')


