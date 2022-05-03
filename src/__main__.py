from utils import time_math
from configuration import Config, reload_settings
from render import Render
import os


def initialisation():
    """Create folder for image output if it does not exist already.
    """
    try:
        os.mkdir('../output')
    except FileExistsError:
        pass

    try:
        os.mkdir('../data')
    except FileExistsError:
        pass


def main():
    render = Render()
    render.batch_rendering(5, re_start=-0.5, re_end=0.5, im_start=-0.75, im_end=0.75)
    path = render.save_image_list()
    render.render_video(path, custom_name="Video")


if __name__ == "__main__":
    initialisation()
    time_math.start_running_time()
    config = Config()
    config.write_default_settings()
    config.modify_settings("display", "width", 1900)
    config.modify_settings("display", "height", 1267)
    reload_settings()
    main()
    time_math.show_running_time()
