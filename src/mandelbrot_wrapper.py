import os
import ctypes
import numpy as np

# Load the shared library
_lib = ctypes.CDLL('./libmandelbrot.so')

# Define the Mandelbrot Set function
def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iterations):
    img = np.empty((height, width), dtype=np.uint8)
    _lib.mandelbrotSet(
        img.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)),
        ctypes.c_int(width),
        ctypes.c_int(height),
        ctypes.c_float(x_min),
        ctypes.c_float(x_max),
        ctypes.c_float(y_min),
        ctypes.c_float(y_max),
        ctypes.c_int(max_iterations)
    )
    return img
