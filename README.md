Fractal App (2D)
===========================================
Fractal App is a simple app to view and play with 2D fractal, as of now only the mandelbrot set. It allow user to specify parameters to generate high-quality image and basic animation. It is plan in the future to make it able to generate animation.  
[Link to main repo](https://github.com/ritonun/ritons-fractal)

# Run program
In order to run the program, please install all the module required.  
`pip install -r requirements.txt`

# Work in progress
- ~~[x] OOP Image calculation~~
- [x] mandelbrot math
- [ ] pygame image viewer OOP
- [x] small animation / zoom incorporation in main.py

# Features to come (maybe, no guarantee)
- color parameters to generate nice looking fractal
- counter on wich iteration we are of the animation, so we can pause it, kill the program and when prgm restarted, continue generate image from the iteration count (useful for very long processing of image)
- script to create gif incorporated into app
- custom output path variable in settings
- viewer (with pygame?) for coordinate, zoom
- optimisation
- logging (instead of debuggin with print)
- executables
- test units (proper one with a library)
- documentation (with mkdocs)

# Roadmap
v0.1.0: Image creation and view  
v0.2.0: Batch image processing to create gif/video  
v0.3.0: Image viewer and interact with image live (zoom, rotation?)  

v1.0.0: Minimal GUI application handling all tha app  

# Changelog
Current version: v0.2.0  

# Docs
Documentation is build with MKdocs. All the `.mk` file are in the `docs/` folder. You can view them nicely by placing yourself in the project folder and entering the command `mkdocs serve`. Then enter in your browser the custom adress showed (something like `http://127.0.0.1:8000`). If you prefer, you can build the site instead of creating a server with the command `mkdocs build`. In the `site/` folder it will create, open `index.html`.  

# Dev links
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
