from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Import from configuration
app.config.from_object('config')


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/events")
def events():
    return render_template('events.html')


@app.route("/info")
def info():
    return render_template('info.html')


@app.route("/libraries")
def libraries():
    return render_template('libraries.html')


@app.route("/schools")
def schools():
    return render_template('schools.html')


@app.route("/officials")
def officials():
    return render_template('officials.html')


@app.context_processor
def inject_ga():
    return dict(GA_ID=app.config["GA_ID"])

if __name__ == "__main__":
    app.run(debug=True)
