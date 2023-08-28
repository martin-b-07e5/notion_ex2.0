# forecast/clean_forecast_data.py
import pandas as pd
from utils.convert_unix_to_day import convert_unix_to_day
from utils.convert_unix_to_time import convert_unix_to_time


def clean_forecast_data(forecast_data_list, timezone_offset):
    cleaned_dataframes = []

    for forecast_item in forecast_data_list:
        # Extract weather information and add a prefix
        weather_info = pd.json_normalize(forecast_item["weather"][0]).add_prefix("weather_")

        # Remove the weather key from forecast data
        del forecast_item["weather"]

        # Convert forecast data to a DataFrame
        forecast_dataframe = pd.json_normalize(forecast_item)

        # Combine weather and forecast dataframes
        combined_dataframe = pd.concat([forecast_dataframe, weather_info], axis=1)

        cleaned_dataframes.append(combined_dataframe)

    # Concatenate all cleaned dataframes
    cleaned_forecast_df = pd.concat(cleaned_dataframes, axis=0)

    # Apply functions to convert Unix timestamps to day names and time strings
    # Unix timestamps in the "dt" column are converted to day names and
    #  time strings using the provided utility functions
    #   (convert_unix_to_day and convert_unix_to_time).
    cleaned_forecast_df["day"] = cleaned_forecast_df["dt"].apply(lambda x: convert_unix_to_day(x, timezone_offset))
    cleaned_forecast_df["time"] = cleaned_forecast_df["dt"].apply(lambda x: convert_unix_to_time(x, timezone_offset))

    # the cleaned DataFrame with additional columns for day names and time strings is returned.
    return cleaned_forecast_df


"""
1. cleaned_forecast_df: This is the DataFrame that you're working with.
2. "day": This is the name of the new column that you're adding to the DataFrame.
3. cleaned_forecast_df["dt"]: This part is selecting the values from
      the existing "dt" column of the DataFrame.
    The "dt" column contains Unix timestamps representing specific points in time.

4. .apply(lambda x: convert_unix_to_day(x, timezone_offset)):
      This part applies a function to each value in the "dt" column.
       The lambda function takes each value x (which is a Unix timestamp) and
        passes it to the convert_unix_to_day function along with the
         timezone_offset argument.

        lambda x: This defines an anonymous function that takes an argument x.

        convert_unix_to_day(x, timezone_offset): This part calls the convert_unix_to_day function with the Unix timestamp x and the timezone_offset argument.
         The function presumably converts the Unix timestamp to a human-readable day format, accounting for the provided timezone offset.

        The result of the convert_unix_to_day function call becomes the value in the new "day" column for each corresponding row.

So, in summary, this line of code calculates the day corresponding to each Unix 
"""
