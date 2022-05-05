Fractal App (2D)
===========================================
Fractal App is a simple app to view and play with 2D fractal, as of now only the mandelbrot set. It allow user to specify parameters to generate high-quality image and basic animation. It is plan in the future to make it able to generate animation.  
[Link to main repo](https://github.com/ritonun/ritons-fractal)

# Features
- Render high-quality fractal image in white & black
- Render batch of image with zoom/dezoom

# Features to come (maybe, no guarantee)
## App features
- color parameters to generate nice looking fractal
- counter on wich iteration we are of the animation, so we can pause it, kill the program and when prgm restarted, continue generate image from the iteration count (useful for very long processing of image)
- script to create gif incorporated into app
- viewer (with pygame?) for coordinate, zoom
- optimisation
## Dev features
- logging (instead of debuggin with print)
- executables
- test units (proper one with a library)
- documentation (with mkdocs)

# Work in progress
v0.3.0: Quality of life imporvement, back-end changes, optimisation  
v0.2.5: script to convert batch image folder into high-quality video format (.gif, .mp4, etc...)  
v0.2.1: Upgrade of batch rendering with better input  
v0.2.0: Batch render of image   

# Roadmap
v0.1.0: Image creation and view  
v0.2.0: Batch image processing 
v0.2.5: Script to convert batch image folder into high quality gif/videos  
v0.3.0: quality of life imporvement, optimisation  
v0.4.0: Image viewer and interact with image live (zoom, rotation?)  

v1.0.0: Minimal GUI application handling all the app  

# Changelog
Current version: v0.2.1  

# Run program
In order to run the program, please install all the module required.  
`pip install -r requirements.txt`  
Then run `main.py` int the `src/` folder.  

# Docs
Documentation is build with MKdocs. All the `.mk` file are in the `docs/` folder. You can view them nicely by placing yourself in the project folder and entering the command `mkdocs serve`. Then enter in your browser the custom adress showed (something like `http://127.0.0.1:8000`). If you prefer, you can build the site instead of creating a server with the command `mkdocs build`. In the `site/` folder it will create, open `index.html`.  

# Dev links
*OOP tkinter*  
https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html  
*documentation:*  
https://docs.readthedocs.io/en/latest/intro/import-guide.html  
https://docs.python-guide.org/writing/documentation/  
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
