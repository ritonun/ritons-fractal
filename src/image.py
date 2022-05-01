from PIL import Image, ImageDraw
import configuration.settings as cs
from fractal_math import mandelbrot
from utils import loading
import datetime
import importlib


def render_image(show_loading=True):
    importlib.reload(cs)
    img = Image.new('RGB', (cs.WIDTH, cs.HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    for x in range(0, cs.WIDTH):
        for y in range(0, cs.HEIGHT):

            c = complex(cs.RE_START + (x / cs.WIDTH) * (cs.RE_END - cs.RE_START),
                        cs.IM_START + (y / cs.HEIGHT) * (cs.IM_END - cs.IM_START))
            m = mandelbrot(c)
            color = 255 - int(m * 255 / cs.MAX_ITER)
            draw.point([x, y], (color, color, color))

        if show_loading:
            loading.show_loading_msg(x, cs.WIDTH)

    return img


def save_image(img, path="../res_dev/output/"):
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    name = path + "mdb" 
    filename = "_".join([name, suffix])
    filename += ".png"
    img.save(filename)
    print("saved in {}".format(filename))
