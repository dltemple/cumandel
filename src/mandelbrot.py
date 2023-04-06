import numpy as np

def mandelbrot_numpy(width, height, x_min, x_max, y_min, y_max, max_iterations, progress_callback=None):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)

    x, y = np.meshgrid(x, y)
    c = x + 1j * y
    z = np.zeros_like(c, dtype=complex)
    mandelbrot = np.zeros_like(c, dtype=int)

    for i in range(max_iterations):
        if progress_callback is not None and i % 10 == 0:
            progress_callback(int(i / max_iterations * 100))

        mask = np.abs(z) <= 2
        z[mask] = z[mask] ** 2 + c[mask]
        mandelbrot[mask] = i

    return mandelbrot
