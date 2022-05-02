
def mandelbrot(c, max_iter):
    """ Calculate wether a number is part of the mandelbrot set or not.
    Return n iteration of the while loop. If n is small, the number is part of
    the fractal. 
    max_iter will make the image more precise the higher it is, but it will 
    slow down the program. max_iter shoul always come from settings parameters.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n
