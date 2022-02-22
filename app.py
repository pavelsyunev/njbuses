from flask import Flask, render_template, url_for, redirect
from parser import get_bus_schedule

app = Flask(__name__)


# app.config['SECRET_KEY'] = 'qasr4r4ed45tfr237787hh343ghgbfgbfgbrt'


@app.route('/')
def index():
    bus_schedule = get_bus_schedule()
    return render_template("index.html", bus_schedule=bus_schedule, bus_stop_name='🚏- Boulevard EAST 66th ST')


@app.route('/<int:bus_stop_id>')
def bus_stop(bus_stop_id):
    bus_schedule = get_bus_schedule(bus_stop_id)
    if bus_stop_id == 21890:
        bus_stop_name = '🚏- Boulevard EAST 66th ST'
    elif bus_stop_id == 32084:
        bus_stop_name = '🚏- Willow AVE 15th ST'
    elif bus_stop_id == 26229:
        bus_stop_name = '🚏- PORT AUTHORITY BUS TERMINAL'
    else:
        bus_stop_name = ''
    return render_template("index.html", bus_schedule=bus_schedule, bus_stop_name=bus_stop_name)


if __name__ == "__main__":
    app.run(debug=True)