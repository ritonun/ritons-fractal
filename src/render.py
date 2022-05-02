from PIL import Image, ImageDraw
import configuration.settings as cs
from configuration import reload_settings
from fractal_math import mandelbrot
from utils import Loading
import datetime


class Render:
    def __init__(self):
        self.list_image = []

    def image(self, show_loading=True, save=False):
        """
        Create an image pixel by pixel based on settings value. 
        show_loading will print to user advancment in % of the image creation.
        
        Args:
            show_loading (bool, optional): Show user advancement in % of the rendering
            save (bool, optional): Automatically save the image once it generate
        
        Returns:
            PIL Image: Image of the mandlebrot set with specified parameters
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

        self.list_image.append(img)
        return img

    def reset_image_list(self):
        """Reset self.list_image[] 
        """
        self.list_image = []

    def save_image_list(self):
        """Save all image of self.list_image[]
        """
        for i in self.list_image:
            self.save_image(i)

    def save_image(self, img, path="../res_dev/output/"):
        """Save the image into the specified path with a auto-generated name 
        
        Args:
            img (PIL Image): Image
            path (str, optional): Output path where the image will be located
        """
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        name = path + "mdb" 
        filename = "_".join([name, suffix])
        filename += ".png"
        img.save(filename)
        print("saved in {}".format(filename))
