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

`git clone https://github.com/dltemple/cumandel.git'
`cd cumandel`

2. Install the required Python packages:

`pip install -r requirements.txt`

3. Compile the CUDA C++ code:

`make`

## Usage

1. Run the Flask web application:
`python src/app.py`

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to start exploring the Mandelbrot Set!

## Directory Structure

cumandel/
│
├── include/
│ └── mandelbrot.h
│
├── src/
│ ├── mandelbrot.cu
│ ├── main.cpp
│ ├── mandelbrot_wrapper.py
│ └── app.py
│
├── templates/
│ └── index.html
│
├── Makefile
│
├── requirements.txt
│
└── README.md


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or create an Issue if you have any suggestions, improvements, or bug reports.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
