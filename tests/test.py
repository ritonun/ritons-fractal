import time
import importlib
from "../src/utils" import *


def test_loading_py():
    loading = importlib.import_module(".loading.py", package="src")
    load = loading.Loading(600)
    for i in range(0, 600):
        time.sleep(0.01)
        load.show_loading_msg(i)


# test_loading_py()
