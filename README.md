# CuMandel: GPU-Accelerated Mandelbrot Set Explorer

CuMandel is an interactive Mandelbrot Set explorer that utilizes the power of NVIDIA GPUs through CUDA for fast and efficient fractal rendering. This project also demonstrates how to create a Python wrapper for the CUDA C++ kernel using the ctypes library and integrate it with a Flask web application.

![Mandelbrot Set Image](./assets/mandelbrot-example.png)

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- GPU-accelerated Mandelbrot Set rendering using NVIDIA CUDA
- Interactive exploration with zooming and panning
- Python wrapper for the CUDA kernel using ctypes
- Flask web application for a seamless user experience

## Requirements

- NVIDIA GPU with CUDA support
- [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) (version 10.0 or later)
- Python 3.6 or later
- Flask 1.0 or later

## Installation

1. Clone the repository:

```git clone https://github.com/dltemple/cumandel.git
cd cumandel```