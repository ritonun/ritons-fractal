from utils import time_math
from configuration import Config
from render import Render
import os


def load():
    """Create folder for image output if it does not exist already.
    """
    try:
        os.mkdir('../output')
    except FileExistsError:
        pass


def main():
    render = Render()
    render.batch_rendering(5, re_start=-0.5, re_end=1, im_start=-0.75, im_end=0.75)


if __name__ == "__main__":
    load()
    time_math.start_running_time()
    config = Config()
    config.write_default_settings()
    main()
    time_math.show_running_time()

    '''
    config.modify_settings("fractal", "max_iter", 80)
    config.modify_settings("display", "width", 600)
    config.modify_settings("display", "height", 400)
    anim(5, main, new_re_start=-0.35, new_re_end=-0.08, new_im_start=-0.775, 
         new_im_end=-0.605)
    '''
