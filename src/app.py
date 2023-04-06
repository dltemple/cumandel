from flask import Flask, render_template
from flask_socketio import SocketIO, emit
# from mandelbrot_wrapper import render_mandelbrot_cuda
from mandelbrot import mandelbrot_numpy

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('render_mandelbrot')
def handle_render_mandelbrot(data):
    def progress_callback(progress):
        emit('progress', {'progress': progress}, broadcast=True)

    # if data.get('use_cuda', True):
    #     mandelbrot_data = render_mandelbrot_cuda(
    #         data['width'], data['height'],
    #         data['x_min'], data['x_max'],
    #         data['y_min'], data['y_max'],
    #         data['max_iterations'],
    #         progress_callback
    #     )
    # else:
    mandelbrot_data = mandelbrot_numpy(
        data['width'], data['height'],
        data['x_min'], data['x_max'],
        data['y_min'], data['y_max'],
        data['max_iterations'],
        progress_callback
    )

    emit('rendered_mandelbrot', mandelbrot_data.tolist())

if __name__ == '__main__':
    socketio.run(app, debug=True)
