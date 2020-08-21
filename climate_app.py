import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
measurements = Base.classes.measurement

stations = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__Climate__)

@app.route("/")
def home():
    print("Available routes:")
    print("/api/v1.0/precipitation")
    print("/api/v1.0/stations")
    print("/api/v1.0/tobs")
    print("/api/v1.0/<start>` and `/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(measurements.date, measurements.prcp, measurements.tobs)
    print("")

@app.route("/api/v1.0/stations")
def precipitation():
    print("")

@app.route("/api/v1.0/tobs")
def precipitation():
    print("")
    
@app.route("/api/v1.0/<start>")
def precipitation():
    print("")
    
@app.route("/api/v1.0/<start>/<end>")
def precipitation():
    print("")

