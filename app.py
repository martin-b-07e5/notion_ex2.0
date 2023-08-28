# app.py
from flask import Flask, render_template, request
from utils.api_key_util import api_key_util
from weather.get_weather_fn import get_weather_fn
from weather.process_weather_fn import process_weather_fn
from weather.normalize_weather_fn import normalize_weather_fn
from forecast.get_forecast_fn import get_forecast_fn
from forecast.process_forecast_fn import process_forecast_fn

app = Flask(__name__)

api_key = None
try:
    # ✅ GET THE API KEY.
    api_key = api_key_util()
except Exception as e:
    print("API key error: ", e)


# root
@app.route("/", methods=["GET", "POST"])
def index():
    processed_weather_dict = None
    forecast_dict = None

    if request.method == "POST":
        city = request.form["city"]
        # --------------------------------------------------
        # ✅ get_weather_fn
        weather_dict = get_weather_fn(city, api_key)
        # print("\ntype:", type(weather_dict))
        # print("weather_dict:\n", weather_dict)

        # ✅ process_weather_fn
        processed_weather_dict = process_weather_fn(weather_dict)
        # print("\ntype processed_weather_dict:", type(processed_weather_dict))
        # print("processed_weather_dict:\n", processed_weather_dict)

        # ✅ Call the method that CREATES THE CSV
        normalize_weather_fn(processed_weather_dict)
        # --------------------------------------------------
        # --------------------------------------------------
        # 👷 get_forecast_fn
        forecast_dict = get_forecast_fn(city, api_key)
        print("\ntype forecast_dict: ", type(forecast_dict))
        print("get_forecast_dict:\n", forecast_dict)

        # ✅ process_forecast_fn
        processed_forecast_dict = process_forecast_fn(forecast_dict)
        print("\ntype processed_forecast_dict: ", type(processed_forecast_dict))
        print("processed_forecast_dict\n", processed_forecast_dict)
        # --------------------------------------------------
        # --------------------------------------------------

    return render_template(
        "index.html",
        weather_data=processed_weather_dict,
        forecast_data=forecast_dict,
    )


if __name__ == "__main__":
    app.run()
