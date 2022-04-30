import configparser

DEFAULT_FILEPATH = "../data/settings.ini"


class Config:
    def __init__(self, filepath=DEFAULT_FILEPATH):
        self.filepath = filepath
        self.config = self.read_settings(self.filepath)

    def write_default_settings(self, filepath=DEFAULT_FILEPATH):
        config = configparser.ConfigParser()
        config['display'] = {
            "width": 600,
            "height": 400
        }

        config['fractal'] = {
            "max_iter": 80,
            "re_start": -2,
            "re_end": 1,
            "im_start": -1,
            "im_end": 1
        }

        with open(filepath, "w") as configfile:
            config.write(configfile)
        self.config = config

    def read_settings(self, filepath=DEFAULT_FILEPATH):
        config = configparser.ConfigParser()
        config.read(filepath)
        return config

    def modify_settings(self, section, data, number, filepath=DEFAULT_FILEPATH):  # noqa: E501
        config = configparser.ConfigParser()
        config.read(filepath)
        config.set(section, data, str(number))
        with open(filepath, "w") as configfile:
            config.write(configfile)
        print("--- Config file written successfully ({}) ---".format(filepath))
        self.config = config
