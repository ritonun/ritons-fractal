API
===========

# Utils
## Loading
::: src.utils.Loading
## TimeMath
::: src.utils.TimeMath

::: src.main




# Fractal math
## Mandelbrot set

# Image creation
## render_image()
Create an image pixel by pixel and return it based on the mandelbrot_set

## save_image(img, path="")
Save an image into the path specified. There is a default path if not specified.

# Animation
## anim(iteration, new re & im value)
Create iteration number of image that zoom or dezoom toward the new re & im value specified.

# Configuration
## Config()
This class is to read through a settings.ini file, write default value into it or modify value on it.

## Settings.py
The value of the file depends on the settings.ini value. If they are change, settings.py need to be reload.

## reload_settings()
Reload settings.py value. Useful when a settings value has been changed.

# Utils
## Loading bar
Show user the advancement of a task.  

    loading = Loading()
    loading.show_loading_msg(current_value, max_value)
You need to call loading.show_loading_msg() at each iteration of your for loop.
Example:
    
     loading = Loading()
     for i in range(0, 600):
     	# do task ...
     	loading.show_loading_msg(i, 600)

Import the class:
    
     from utils import Loading

## Execution time
Show user the time of execution of a task/program.

    time_math.start_running_time()
    # do task ...
    time_math.show_running_time()
Import the object:

    from utils import time_math