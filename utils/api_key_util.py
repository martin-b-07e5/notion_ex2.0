# api_key_util.py
import configparser
import pathlib


def api_key_util():
    # https://www.pythonanywhere.com/forums/topic/30771/#id_post_100134
    # Using pathlib to find the absolute path to my app and append "config.ini"
    #  to the end. This way it works locally and remote.
    # config_path = pathlib.Path(__file__).parent.absolute() / "config.ini"

    # Creates a ConfigParser object.
    config = configparser.ConfigParser()
    # Read the configuration file.
    config.read('config.ini')
    # config.read(config_path)

    # Get API key from config.ini configuration file.
    api_key = config.get('WeatherAPI', 'api_key')

    return api_key
