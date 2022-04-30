import time
import src.utils


def test_loading_py():
    load = src.utils.Loading()
    for i in range(0, 600):
        time.sleep(0.01)
        load.show_loading_msg(i, 600)


test_loading_py()
