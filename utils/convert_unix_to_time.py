from datetime import datetime


def convert_unix_to_time(unix_timestamp, tz):
    formatted_time = datetime.utcfromtimestamp(unix_timestamp + tz).strftime("%H:%M:%S")
    return formatted_time
