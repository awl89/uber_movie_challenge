Uber coding challenge - SF Movie 
=============================
Create a service that shows on a map where movies have been filmed in San Francisco. The user should be able to filter the view using autocompletion search.

The data is available on [DataSF](http://www.datasf.org/): [Film
Locations](https://data.sfgov.org/Arts-Culture-and-Recreation-/Film-Locations-in-San-Francisco/yitu-d5am).

Demo
------
A live demo can be found [here](http://boiling-ravine-69107.herokuapp.com)

Features
--------
The following features have been implemented:
- Implemented the map service with the filter function (the base requirement)
- Added a view to create new movies
- Added a view to list all the movies. This view uses a simple cache to store previous requests.

Technologies used
------------------
The following technologies have been used:
- Backend language: Python 2.7
- Backend framework: Flask
- Database: PostgreSQL

For python dependencies see: requirements.txt.
Install the dependencies by running: pip install requirements.txt

Run the web application
-------------------------
To run the web application in developer mode (i.e. where stuff like debugging etc. is enabled), follow the following steps:
- set up a postgres database
- fill out the data base informations in "config.py" within the class "DevConfig"
- run the command "python main.py db", which will create the database table and populate it with data.
- run "python main.py dev" to start the web server
- access the server at "http://localhost:5000"

Run the test cases
--------------------
To run the test cases, follow the following steps:
- set up a postgres test database
- fill out the data base informations in "config.py" within the class "DevConfig" (probably use the same as in the case above)
- run the command "python main.py db", which will create the database table and populate it with data.
- run: python main.py test
