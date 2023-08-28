# convert_unix_to_day.py
from datetime import datetime


def convert_unix_to_day(unix_timestamp, tz):
    day_names = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    formatted_day = datetime.utcfromtimestamp(unix_timestamp + tz).weekday()
    return day_names[formatted_day]
