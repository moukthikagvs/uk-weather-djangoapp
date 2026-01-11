# UK Weather Data Django Application

This project is a Django-based application that parses summarized UK weather data from the UK MetOffice, stores it in a PostgreSQL database, and serves the data via RESTful APIs. A simple frontend is provided for accessing and visualizing the weather dat

# Features

 Parses UK MetOffice climate data (Tmax, Tmin)
 Stores data in PostgreSQL
 RESTful API using Django REST Framework
 Filter weather data by year, parameter, and region
 Simple frontend for data access and visualization


# Tech Stack

 Python
 Django
 Django REST Framework
 PostgreSQL
 Pandas
 HTML + JavaScript

# Data Source

UK MetOffice Climate Datasets:  
https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-regional-series

Example dataset:  
https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt


# Local Setup
1. Clone repository
```bash
git clone https://github.com/moukthikagvs/uk-weather-djangoapp.git
cd uk-weather-djangoapp/config
