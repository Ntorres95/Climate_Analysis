import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
measurements = Base.classes.measurement

stations = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

app = Flask(__name__)

#home route
@app.route("/")
def home():
    return(
        f'Available routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/start and /api/v1.0/start/end'
    )

#route for precip info
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    #query the date and precip data
    results = session.query(measurements.date, measurements.prcp).all()
    session.close()

     # lists for the dictionary
    date_list = []
    prcp_list = []
    
    #loop to fill in the lists
    for date, prcp in results:
        date_list.append(date)
        prcp_list.append(prcp)
    
    #create the dictionary
    prcp_dict = dict(zip(date_list, prcp_list))

    #return the jsonified list
    return jsonify(prcp_dict)

#route for station info
@app.route("/api/v1.0/stations")
def stations_json():
    
    #query the station results
    results = session.query(stations.station).all()
    session.close()
    
    #list for station info
    station_list = []
    
    #loop to collect the station info
    for station in results:
        station_list.append(station)
    
    #return the jsonified list
    return jsonify(station_list)

#route for temp info
@app.route("/api/v1.0/tobs")
def temperature():
    
    # Calculate the date 1 year ago from the last data point in the database
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    #query results
    results = session.query(measurements.date, measurements.tobs).\
        filter(measurements.date >= query_date).\
        filter(measurements.station=='USC00519281')
    session.close()
    
    #list for the temp info
    tobs_list = []
    
    #loop to collect temp info
    for tobs in results:
        tobs_list.append(tobs)
    
    #return the jsonified list
    return jsonify(tobs_list)
    
#route for temp info based on start date
@app.route("/api/v1.0/<start>")
def temp_start(start):
    
    #query results based on start date
    results = session.query(measurements.date, measurements.tobs).\
        filter(measurements.date >= start)
    session.close()
    
    #list for temp data
    tobs_list = []
    
    #loop to collect data for temp data
    for tobs in results:
        tobs_list.append(tobs)

    #return the jsonified list
    return jsonify(tobs_list)
    
#route for temp data based on start and end dates
@app.route("/api/v1.0/<start>/<end>")
def temp_segment(start, end):
    
    #query the temp data
    results = session.query(measurements.date, measurements.tobs).\
        filter(measurements.date >= start).\
        filter(measurements.date <= end)
    session.close()
    
    #list for the temo data
    tobs_list = []
    
    #loop to save the temp results
    for tobs in results:
        tobs_list.append(tobs)
    
    #return the jsonified list
    return jsonify(tobs_list)

if __name__ == '__main__':
    app.run(debug=True)
