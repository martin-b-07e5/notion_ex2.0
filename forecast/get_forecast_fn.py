# forecast/get_forecast_fn.py
import requests


def get_forecast_fn(city, api_key):
    base_url = f"https://api.openweathermap.org/data/2.5/forecast"
    params_dict = {"q": city, "units": "metric", "lang": "en", "appid": api_key}

    try:
        response = requests.get(base_url, params_dict)
        data = response.json()

        return data  # json completo

    except Exception as e:
        print("get_forecast_fn Exception", e)
