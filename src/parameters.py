import configparser

DEFAULT_FILEPATH = "../data/settings.ini"


class Config:
    def __init__(self, filepath=DEFAULT_FILEPATH):
        self.filepath = filepath
        self.config = self.read_settings(self.filepath)

    def write_default_settings(self):
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

        with open(self.filepath, "w") as configfile:
            config.write(configfile)
        self.config = config

    def read_settings(self, filepath=None):
        if filepath is None:
            path = self.filepath
        else:
            path = filepath
        config = configparser.ConfigParser()
        config.read(path)
        return config

    def modify_settings(self, section, data, number):  # noqa: E501
        config = configparser.ConfigParser()
        config.read(self.filepath)
        config.set(section, data, str(number))
        with open(self.filepath, "w") as configfile:
            config.write(configfile)
        print("--- Config file written successfully ({}) ---".format(self.filepath))
        self.config = config
