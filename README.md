Fractal App (2D)
===========================================
Fractal App is an simple app to view and play with 2d fractal, as of now only the mandelbrot set. It allow user to specify parameters to generate high-quality image.  
It is plan in the future to make it able to generate animation.  
[Link to main repo](https://github.com/ritonun/ritons-fractal)

# Features to come

# Links
*documentation:*  
https://docs.readthedocs.io/en/latest/intro/import-guide.html  
*project structure:*  
https://docs.python-guide.org/writing/structure/  
*color:*  
https://www.codingame.com/playgrounds/2358/how-to-plot-the-mandelbrot-set/adding-some-colors  
*math:*  
https://www.youtube.com/watch?v=NGMRB4O922I  
*unit test:*  
https://realpython.com/python-testing/  
*research google:*  
profile code  
optimisze pillow image  

# Docs

### Src

### Utils
Package that contains useful small class.  

* TimeMath()  -> when init it start a timer  
Class to print to screen the time of execution of a program  
start_running_time() -> reset timer  
show_running_time(reset=False) -> show time of execution, if reset it reset the timer  

* Loading() 
Class to print to user loading msg in % during a task  
show_loading_msg(current_value, max_value)  
    Convert a value into a % to show user advancement every x time  
    current_value: current iteration in the for loop  
    max_value:  max value possible for the iteration  


