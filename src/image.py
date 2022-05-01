from PIL import Image, ImageDraw
from configuration import WIDTH, HEIGHT, RE_START, RE_END, IM_START, IM_END, MAX_ITER
from fractal_math import mandelbrot
from utils import loading


def render_image(save=False, show=True):
    img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):

            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))

            m = mandelbrot(c)

            color = 255 - int(m * 255 / MAX_ITER)

            draw.point([x, y], (color, color, color))
        loading.show_loading_msg(x, WIDTH)

    return img
