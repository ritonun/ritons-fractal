from PIL import Image, ImageDraw
import configuration.settings as cs
from configuration import reload_settings, Config
from fractal_math import mandelbrot
from utils import Loading
import datetime
import os
import moviepy.video.io.ImageSequenceClip


def generate_name(name):
    """Generate a custom name based on datetime
    
    Args:
        name (str): Custom name str will begin with
    
    Returns:
        str: return str with: name_YEARMONTHDAY_HOURMINUTESSECONDS_
    """
    name += "_"
    name += datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    name += "_"
    return name


class Render:

    """Handle image rendering and batch image rendering.
    
    Attributes:
        list_image (list): Contains all image created by batch_rendering()
    """
    
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

    def show_image_list(self):
        self.list_image[0].show()

    def reset_image_list(self):
        """Reset self.list_image[] 
        """
        self.list_image = []

    def save_image_list(self):
        """Save all image of self.list_image[]
        """
        index = 0
        folder_name = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        path_folder = cs.DEFAULT_PATH + "/" + folder_name
        os.mkdir(path_folder)
        print(path_folder)
        for i in self.list_image:
            self.save_image(i, index=index, folder_name=folder_name)
            index += 1
        return path_folder

    def save_image(self, img, index=None, folder_name=""):
        """Save the image into the default path with a auto-generated name.
        Naming make sure that no file are overwritten.
        
        Args:
            img (PIL Image): Image
            index (int): Number of image process. Number is added at the end
            folder_name (str, optional): Folder output name, only use for batch saving file.
            of the file name to avoid overwriting existing img.
        """

        filename = cs.DEFAULT_PATH + "/"
        if folder_name != "":
            filename += folder_name + "/"
        filename += generate_name("fractal")
        if index is not None:
            filename += "(" + str(index) + ")"
        filename += ".png"

        img.save(filename)
        print("Saved in {}".format(filename))

    def batch_rendering(self, iteration, **kwargs):
        """Render iteration number of image. the **kwargs value specify new 
        value for RE_START, RE_END, IM_START and IM_END. It will create each 
        image with a zoom/dezoom until it reach the new value. All the image 
        can then be combine into a gif or video.
        
        Args:
            iteration (int): number of image created. The higher the number, 
                             the smoother the animation will be.
            **kwargs: 4 value possible: re_start, re_end, im_start, im_end. 
                      Enter the final value we want to zoom/dezoom to.
        
        Raises:
            Exception: Raise error if one of the kwargs is not what is expected.
        """
        loading = Loading()
        reload_settings()
        config = Config()

        incrementation = {}
        for key in kwargs:
            if key == "re_start":
                incrementation['re_start'] = (cs.RE_START - kwargs[key]) / iteration
            elif key == "re_end":
                incrementation['re_end'] = (cs.RE_END - kwargs[key]) / iteration
            elif key == "im_start":
                incrementation['im_start'] = (cs.IM_START - kwargs[key]) / iteration
            elif key == "im_end":
                incrementation['im_end'] = (cs.IM_END - kwargs[key]) / iteration
            else:
                raise Exception("Name of variable for **kwargs in render.batch_render is not possible")  

        for i in range(0, iteration):
            for key in kwargs:
                if key == "re_start":
                    config.modify_settings("fractal", "re_start", cs.RE_START - incrementation['re_start'])
                if key == "re_end":
                    config.modify_settings("fractal", "re_end", cs.RE_END - incrementation['re_end'])
                if key == "im_start":
                    config.modify_settings("fractal", "im_start", cs.IM_START - incrementation['im_start'])
                if key == "im_end":
                    config.modify_settings("fractal", "im_end", cs.IM_END - incrementation['im_end'])

            reload_settings()
            loading.show_loading_msg(i, iteration, custom_msg="Animation:")
            self.image()

    def render_video(self, fps, path):
        image_folder = path
        fps = fps
        output_folder_name = "../output/" + generate_name("video") + ".mp4"

        images_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png")]
        images_files = sorted(images_files)
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(images_files, fps=fps)
        clip.write_videofile(output_folder_name)
