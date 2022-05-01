from configuration import config
from utils import time_math
from image import render_image


def main():
    time_math.start_running_time()
    im = render_image()
    time_math.show_running_time()
    im.show()


if __name__ == "__main__":
    main()
