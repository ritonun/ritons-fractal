import time
import src.utils


def test_loading_msg():
    load = src.utils.Loading()
    for i in range(0, 600):
        time.sleep(0.01)
        load.show_loading_msg(i, 600)


def test_runtime():
    sleep_time = 5
    myTime = src.utils.TimeMath()
    time.sleep(5)
    runtime = myTime.show_running_time()
    if runtime > sleep_time and runtime < sleep_time + 1:
        print("Test runtime: OK!")
    else:
        print("Error: test runtime")


# test_loading_msg()
test_runtime()
