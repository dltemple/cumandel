from flask import Flask, render_template, request, jsonify
from mandelbrot_wrapper import mandelbrot_set

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mandelbrot', methods=['POST'])
def mandelbrot():
    data = request.get_json()
    width = data['width']
    height = data['height']
    x_min = data['x_min']
    x_max = data['x_max']
    y_min = data['y_min']
    y_max = data['y_max']
    max_iterations = data['max_iterations']

    img = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iterations)

    return jsonify(img.tolist())

if __name__ == '__main__':
    app.run(debug=True)
