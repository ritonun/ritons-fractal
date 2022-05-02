from .settings import *
from .parameters import Config
import configuration.settings as cs
import importlib


def reload_settings():
    importlib.reload(cs)
