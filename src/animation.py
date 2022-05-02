from configuration import Config, reload_settings
import configuration.settings as cs
from utils import Loading


def anim(iteration, func, new_re_start=None, new_re_end=None, 
         new_im_start=None, new_im_end=None):
    """
    Take  argument for value of re and im. It will generate iteration amount of
    image that progressively zoom in. Can be coupled to a script to generate 
    gif/video.
    
    Args:
        iteration (int): Number of image created
        func (Function): Function called to create the image each loop 
        new_re_start (int, optional): new re_start value
        new_re_end (int, optional): new re_end value
        new_im_start (int, optional): new im_start value
        new_im_end (int, optional): new im_end value
    """
    loading = Loading()
    reload_settings()
    config = Config()
    incrementation = {}  # incrementation value is calculated before the loop as it is consistent
    if new_re_start is not None:
        incrementation['re_start'] = (cs.RE_START - new_re_start) / iteration
    if new_re_end is not None:
        incrementation['re_end'] = (cs.RE_END - new_re_end) / iteration
    if new_im_start is not None:
        incrementation['im_start'] = (cs.IM_START - new_im_start) / iteration
    if new_im_end is not None:
        incrementation['im_end'] = (cs.IM_END - new_im_end) / iteration

    for i in range(0, iteration):
        if new_re_start is not None:
            config.modify_settings("fractal", "re_start", cs.RE_START - incrementation['re_start'])
        if new_re_end is not None:
            config.modify_settings("fractal", "re_end", cs.RE_END - incrementation['re_end'])
        if new_im_start is not None:
            config.modify_settings("fractal", "im_start", cs.IM_START - incrementation['im_start'])
        if new_im_end is not None:
            config.modify_settings("fractal", "im_end", cs.IM_END - incrementation['im_end'])

        reload_settings()
        func()
        loading.show_loading_msg(i, iteration, custom_msg="Animation: ")
