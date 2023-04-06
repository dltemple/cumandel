#include <iostream>
#include "mandelbrot.h"

int main() {
    // Test the mandelbrotSet function
    int width = 800;
    int height = 600;
    unsigned char *img = new unsigned char[width * height];

    float x_min = -2.0;
    float x_max = 1.0;
    float y_min = -1.0;
    float y_max = 1.0;
    int max_iterations = 1000;

    mandelbrotSet(img, width, height, x_min, x_max, y_min, y_max, max_iterations);

    // Process the img data or save it as an image file

    delete[] img;
    return 0;
}
