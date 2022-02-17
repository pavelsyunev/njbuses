from flask import Flask, render_template, url_for
from parser import get_bus_schedule

app = Flask(__name__)


@app.route('/')
def index():
    bus_schedule = get_bus_schedule()
    return render_template("index.html", bus_schedule=bus_schedule)


if __name__ == "__main__":
    app.run(debug=True)