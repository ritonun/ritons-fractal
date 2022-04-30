import time
import src.utils


def test_loading_msg():
    load = src.utils.Loading()
    for i in range(0, 600):
        time.sleep(0.01)
        load.show_loading_msg(i, 600)


def test_runtime():
    myTime = src.utils.TimeMath()
    time.sleep(5)
    myTime.show_running_time()
    print("result should be 5 sec")


# test_loading_msg()
# test_runtime()
