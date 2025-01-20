# sqlalchemy-challenge

# Outline
------------------------------------------
This challenge aims to explore and analyze climate data using SQLAlchemy ORM for queries, and Python’s Pandas and Matplotlib for data manipulation and visualization. A Flask API is built to house all the collected data.

# Data Source
------------------------------------------
Database: https://github.com/Jagar513/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite

# Tools
------------------------------------------
Python Libraries: SQLAlchemy, Pandas and Matplotlib
Web Framework: Flask


# Part 1: Analyze and Explore the Climate Data
------------------------------------------
Precipitation Analysis

![image](https://github.com/user-attachments/assets/c26d9a0a-6b97-4543-a002-854b043e2ad5)

Summary Statistics

![image](https://github.com/user-attachments/assets/7a4660fb-6a28-4514-be7b-32eadf14046f)

Temperature Analysis

![image](https://github.com/user-attachments/assets/8c8dcada-6969-4c7e-9f9c-c9df547dd9f7)

The station ID that has the greatest number of observations is USC00519281.

The lowest temperature is 54.0.

The highest temperature is 85.0.

The average temperature is 71.66378066378067.

------------------------------------------

# Part 2: Design Your Climate App

---

## Available Routes

- `/api/v1.0/precipitation`
- `/api/v1.0/stations`
- `/api/v1.0/tobs`
- `/api/v1.0/temp/start`
- `/api/v1.0/temp/start/end`

---

### **/api/v1.0/precipitation**

**Description:**  
Returns a JSON representation of the precipitation data from the past year.

**Format:**  
The query results are returned as a list of dictionaries, where each dictionary contains:

- `date`: The date of the observation.
- `prcp`: The precipitation value for that day.

---

### **/api/v1.0/stations**

**Description:**  
Returns a JSON list of all stations present in the dataset.

**Format:**  
A list of station identifiers.

---

### **/api/v1.0/tobs**

**Description:**  
Returns temperature observations (TOBS) for the previous year, based on the most recent data point in the dataset.

**Format:**  
A list of dictionaries, where each dictionary contains:

- `date`: The date of the observation.
- `tobs`: The temperature on that day.

---

### **/api/v1.0/temp/start**

**Description:**  
Returns a JSON list containing the minimum, average, and maximum temperatures for all dates on or after the provided start date.

**Format:**  
A list containing the following values:

- `min`: Minimum temperature.
- `avg`: Average temperature.
- `max`: Maximum temperature.

---

### **/api/v1.0/temp/start/end**

**Description:**  
Returns a JSON list containing the minimum, average, and maximum temperatures for a given date range, between and including the start and end dates.

**Format:**  
A list containing the following values:

- `min`: Minimum temperature.
- `avg`: Average temperature.
- `max`: Maximum temperature.











