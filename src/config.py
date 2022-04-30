import configparser

FILEPATH = "../res/settings.ini"


def write_default_settings(filepath=FILEPATH):
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

    print("--- Config file written successfully ({}) ---".format(filepath))


def read_settings(filepath=FILEPATH):
    config = configparser.ConfigParser()
    config.read(filepath)
    return config


def modify_settings(section, data, number, filepath=FILEPATH):
    config = configparser.ConfigParser()
    config.read(filepath)
    config.set(section, data, str(number))
    with open(filepath, "w") as configfile:
        config.write(configfile)
    print("--- Config file written successfully ({}) ---".format(filepath))


write_default_settings()
config = read_settings()
