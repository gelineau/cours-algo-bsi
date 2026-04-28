import json
from pprint import pprint

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


print(get_coordinates("Rennes"))
