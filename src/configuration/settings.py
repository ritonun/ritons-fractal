''' --- SETTINGS --- '''
from .parameters import Config


def get_int_value(section, key):
    """ Transform config value into a int """
    conf = Config()
    config = conf.read_settings()
    value = config[section][key]
    value = int(value)
    return value


def get_float_value(section, key):
    """ Transform config value into a float """
    conf = Config()
    config = conf.read_settings()
    value = config[section][key]
    value = float(value)
    return value


def get_str_value(section, key):
    conf = Config()
    config = conf.read_settings()
    value = config[section][key]
    return value


# Display
WIDTH = get_int_value("display", "width")
HEIGHT = get_int_value("display", "height")

# Fractal value
# Plot window (RE = x_axis, IM = y__axis)
# Default value: RE_S=-2, RE_E=1, IM_S=-1, IM_E=1, MAX_ITER = 80
RE_START = get_float_value("fractal", "re_start")
RE_END = get_float_value("fractal", "re_end")
IM_START = get_float_value("fractal", "im_start")
IM_END = get_float_value("fractal", "im_end")
MAX_ITER = get_int_value("fractal", "max_iter")

# User
DEFAULT_PATH = get_str_value("user", "default_path")
