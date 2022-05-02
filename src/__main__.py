from utils import time_math
from image import render_image, save_image
from animation import anim
from configuration import Config


def main():
    im = render_image(show_loading=True)
    save_image(im)


if __name__ == "__main__":
    time_math.start_running_time()
    config = Config()
    config.write_default_settings()
    config.modify_settings("fractal", "max_iter", 80)
    config.modify_settings("display", "width", 600)
    config.modify_settings("display", "height", 400)
    anim(5, main, new_re_start=-0.35, new_re_end=-0.08, new_im_start=-0.775, 
         new_im_end=-0.605)
    time_math.show_running_time()
