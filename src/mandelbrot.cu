#include <cuda_runtime.h>
#include <device_launch_parameters.h>

__global__ void mandelbrotKernel(unsigned char *img, const int width, const int height, const float x_min, const float x_max, const float y_min, const float y_max, const int max_iterations) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int idy = blockIdx.y * blockDim.y + threadIdx.y;
    int index = idy * width + idx;

    if (idx < width && idy < height) {
        float x = x_min + (x_max - x_min) * idx / (width - 1);
        float y = y_min + (y_max - y_min) * idy / (height - 1);

        float real = x;
        float imag = y;
        int value = 0;

        for (int i = 0; i < max_iterations; i++) {
            float r2 = real * real;
            float i2 = imag * imag;

            if (r2 + i2 > 4.0f) {
                break;
            }

            imag = 2 * real * imag + y;
            real = r2 - i2 + x;

            value++;
        }

        img[index] = static_cast<unsigned char>((value % 256));
    }
}
