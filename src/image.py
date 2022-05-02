from PIL import Image, ImageDraw
import configuration.settings as cs
from configuration import reload_settings
from fractal_math import mandelbrot
from utils import Loading
import datetime


def render_image(show_loading=True):
    """
    Create an image pixel by pixel based on settings value. 
    show_loading will print to user advancment in % of the image creation.
    """
    loading = Loading()
    reload_settings()
    img = Image.new('RGB', (cs.WIDTH, cs.HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    for x in range(0, cs.WIDTH):
        for y in range(0, cs.HEIGHT):

            c = complex(cs.RE_START + (x / cs.WIDTH) * (cs.RE_END - cs.RE_START),
                        cs.IM_START + (y / cs.HEIGHT) * (cs.IM_END - cs.IM_START))
            m = mandelbrot(c, cs.MAX_ITER)
            color = int(m * 255 / cs.MAX_ITER)
            draw.point([x, y], (color, color, color))

        if show_loading:
            loading.show_loading_msg(x, cs.WIDTH, custom_msg="   ")

    return img


def save_image(img, path="../res_dev/output/"):
    """ Save the image into the specified path with a auto-generated name """
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    name = path + "mdb" 
    filename = "_".join([name, suffix])
    filename += ".png"
    img.save(filename)
    print("saved in {}".format(filename))
