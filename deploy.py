from flask import Flask, render_template, request
from werkzeug.serving import run_simple
app = Flask(__name__)


from bus_algo import bus_algo



@app.route('/')
def form():
   return render_template('form.html')


@app.route('/submit_bus_data', methods=['POST'])
def submit_bus_data():
	starting_station = request.form['starting_station']
	last_station = request.form['last_station']
	bus_array = bus_algo(starting_station, last_station)
	return render_template('display.html', bus_array=bus_array)






# if __name__ == '__main__':
#    run_simple('localhost',5001, app)


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run('localhost', 5001, debug=True)
