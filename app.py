# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt
import pandas as pd
import numpy as np

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Find the most recent date in the data set.
    most_recent_date = session.query(func.max(Measurement.date)).all()
    most_recent_date = most_recent_date[0][0]  # Extract the date from the tuple
    
    # Calculate the date one year from the last date in the data set.
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d").date() - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).order_by(Measurement.date).all()

    # Convert the query results to a dictionary using date as the key and prcp as the value.
    prcp_data = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_data.append(prcp_dict)

    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():
    # Return a JSON list of stations from the dataset.
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Find the most recent date in the data set.
    most_recent_date = session.query(func.max(Measurement.date)).all()
    most_recent_date = most_recent_date[0][0]  # Extract the date from the tuple
    
    # Calculate the date one year from the last date in the data set.
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d").date() - dt.timedelta(days=365)

    # Query the dates and temperature observations of the most active station for the last year of data.
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()
    most_active_station = most_active_station[0]

    most_active_station_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()

    # Return a JSON list of temperature observations (TOBS) for the previous year.
    tobs_data = []
    for date, tobs in most_active_station_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_data.append(tobs_dict)

    return jsonify(tobs_data)

@app.route("/api/v1.0/temp/<start>")
def start(start):
    try:
        # Ensure the start parameter is properly formatted as a date
        start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
        
        # Define the selection of temperature data
        sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
        
        # Query the database for min, avg, max temperatures starting from start_date
        temp_data = session.query(*sel).filter(Measurement.date >= start_date).all()
        
        # Flatten the result from the tuple and prepare it for JSON output
        temp_data_list = [temp for temp in temp_data[0]]  # Get the first (and only) tuple from the results
        
        # Return the JSON response
        return jsonify(temp_data_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/v1.0/temp/<start>/<end>")
def start_end(start, end):
    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end, '%Y-%m-%d').date()
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    temp_data = session.query(*sel).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    temp_data_list = list(np.ravel(temp_data))
    return jsonify(temp_data_list)

if __name__ == '__main__':
    app.run(debug=True)


