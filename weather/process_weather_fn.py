# weather/process_weather_fn.py
from utils.convert_unix_to_time import convert_unix_to_time


# https://openweathermap.org/current#name
def process_weather_fn(weather_data_dict):
    try:
        if weather_data_dict["cod"] == 200:
            timezone = weather_data_dict["timezone"]
            processed_data = {
                "city": weather_data_dict["name"],
                "country": weather_data_dict["sys"]["country"],
                "description": weather_data_dict["weather"][0]["description"],
                "temperature": weather_data_dict["main"]["temp"],
                "humidity": weather_data_dict["main"]["humidity"],
                "pressure": weather_data_dict["main"]["pressure"],
                "wind_speed": weather_data_dict["wind"]["speed"],
                "icon": weather_data_dict["weather"][0]["icon"],
                "sunrise": convert_unix_to_time(weather_data_dict["sys"]["sunrise"], timezone),
                "sunset": convert_unix_to_time(weather_data_dict["sys"]["sunset"], timezone),
            }
            return processed_data
    except Exception as e:
        print("Error from process_WEATHER_data: ", e)
