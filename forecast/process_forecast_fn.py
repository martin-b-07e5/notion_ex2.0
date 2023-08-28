# forecast/process_forecast_fn.py
from forecast.clean_forecast_data import clean_forecast_data


# https://openweathermap.org/forecast5#name5
def process_forecast_fn(forecast_data_dict):
    try:
        # here 200 must be a string
        if forecast_data_dict["cod"] == "200":
            list_forecast = forecast_data_dict["list"]  # complete json
            timezone_city = forecast_data_dict["city"]["timezone"]

            # Call the function clean_forecast_data
            processed_forecast_data = clean_forecast_data(
                list_forecast,
                timezone_city
            )
            return processed_forecast_data
    except Exception as e:
        print("Error from process_FORECAST_data: ", e)
