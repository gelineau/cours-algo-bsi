import json
from pprint import pprint
from typing import Any

import requests

# Force no proxy
proxies = {"http": None, "https": None}


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
    response = requests.get(url, headers=headers, params=params, proxies=proxies)

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

    response = requests.get(url, params=params, proxies=proxies)
    data = json.loads(response.text)
    # pprint(data)

    return (
        data["daily"]["temperature_2m_max"][0],
        data["daily"]["temperature_2m_min"][0],
        data["daily"]["precipitation_sum"][0],
    )


def fetch_activities() -> list[str]:
    url = "https://bored-api.appbrewery.com/filter"

    params = {"type": "recreational"}
    response = requests.get(url, params=params, proxies=proxies)
    data = json.loads(response.text)
    activities = [detailed_activity["activity"] for detailed_activity in data]
    return activities


def send_question(api_key: str, question: str) -> str:
    # Build the request payload
    payload = {
        "model": "mistral-small-latest",
        "messages": [{"role": "user", "content": question}],
    }
    data = json.dumps(payload)

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers,
        data=data,
        timeout=30,
        proxies=proxies,
    )

    result = json.loads(response.text)
    pprint(result)
    return result["choices"][0]["message"]["content"]


def main() -> None:
    city = "Rennes"

    latitude, longitude = get_coordinates(city)
    tomorrow = "2026-04-29"

    weather = fetch_weather_forecast(latitude, longitude, tomorrow)
    print(weather)

    activities = fetch_activities()
    pprint(activities)

    question = f"""
    je suis à Rennes et je veux m'occuper.
    la température maximum sera {weather[0]} minimum {weather[1]}
    et la pluviométrie {weather[2]}. Quelle activité me conseilles-tu parmi
    {activities}
    Donne-moi une réponse concise
    """

    mistral_api_key = "TBC"
    response = send_question(mistral_api_key, question)
    print(response)


main()
