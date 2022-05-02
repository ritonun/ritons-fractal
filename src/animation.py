from configuration import Config, reload_settings
import configuration.settings as cs
from utils import Loading


def anim(iteration, func, new_re_start=None, new_re_end=None, 
         new_im_start=None, new_im_end=None):
    ''' Take new re and im value, and create x image that progressively zoom 
    in, so you can create a gif/video by combining all image '''
    loading = Loading()
    reload_settings()
    config = Config()
    incrementation = {}
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
