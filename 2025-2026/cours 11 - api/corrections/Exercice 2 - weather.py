import json
from pprint import pprint
from typing import Any

import requests


def get_coordinates(city: str) -> tuple[float, float]:
    """
    Convert a city name into latitude and longitude using an API.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1,
    }
    headers = {"User-Agent": "python-weather-example"}
    response = requests.get(url, headers=headers, params=params)

    #     print(
    #         f"""{response.status_code=}
    # {response.text=}"""
    #     )

    data = json.loads(response.text)
    # pprint(data)

    latitude = float(data[0]["lat"])
    longitude = float(data[0]["lon"])
    return latitude, longitude


def fetch_weather_forecast(
    latitude: float, longitude: float, date: str
) -> tuple[float, float, float]:
    """Fetch daily weather forecast for a specific date and coordinates."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "start_date": date,
        "end_date": date,
    }

    response = requests.get(url, params=params)
    data = json.loads(response.text)
    # pprint(data)

    return (
        data["daily"]["temperature_2m_max"][0],
        data["daily"]["temperature_2m_min"][0],
        data["daily"]["precipitation_sum"][0],
    )


def main() -> None:
    city = "Rennes"

    latitude, longitude = get_coordinates(city)
    tomorrow = "2026-04-29"

    weather = fetch_weather_forecast(latitude, longitude, tomorrow)
    print(weather)


main()
