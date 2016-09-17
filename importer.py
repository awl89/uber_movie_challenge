import numpy as np
import pandas as pd
import datetime
import json
import urllib2

from app import *
from conf import *
from app.models import MovieModel

'''
Helper functions
'''
SF_MOVIE_URL = "https://data.sfgov.org/resource/wwmu-gmzc.json"
LOCAL_FILE = "sf_movie_data"

def nan_check(cell):
    return "" if pd.isnull(cell) else cell

def print_data(rows = 20):
    raw_data = pd.read_json(SF_MOVIE_URL)
    print raw_data.head(n = rows)

'''
Parsing stuff:
    1. Parse data 
    2. Get the lat (latitude) and lng (longitude) coordinates
    3. Store locally
'''
def parser():
    df = pd.read_json(SF_MOVIE_URL)
    # drop rows with NaN values in 'locations' column
    df = df.dropna(subset=['locations']) 
    # set other nan values to empty string
    df = df.replace(np.nan,' ', regex=True)
    df['lat'] = ''
    df['lng'] = ''

    API_KEY = BaseConfig.API_KEY
    for index, row in df.iterrows():
        location = row["locations"]
        location_utf8 = urllib2.quote(location.encode("utf8"))
        
        request = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location_utf8 + ",+San+Francisco,+CA&key=" + API_KEY
        response = json.load(urllib2.urlopen(request))

        if len(response['results']) == 0:
            continue
        print index

        coordinates = response['results'][0]['geometry']['location']
        lat = float(coordinates['lat'])
        lng = float(coordinates['lng'])

        df.set_value(index, 'lat', lat)
        df.set_value(index, 'lng', lng)
    df.to_json(LOCAL_FILE+'.json', orient='records')


'''
Store data into the database
'''
def populate_database():
    configure_app("dev")
    db.create_all()

    df = pd.read_json(LOCAL_FILE+'.json')
    df = df[df.lat != '']
    df = df[df.lng != '']

    for index, row in df.iterrows():
        movie = MovieModel(title = row["title"],
                year = int(row["release_year"]),
                location = row["locations"],
                fact = row["fun_facts"],
                company = row["production_company"],
                distributor = row["distributor"],
                director = row["director"],
                writer = row["writer"],
                actor1 = row["actor_1"],
                actor2 = row["actor_2"],
                actor3 = row["actor_3"],
                lng = float(row["lng"]),
                lat = float(row["lat"]))

        db.session.add(movie)
    db.session.commit()

if __name__ == '__main__':
    parser()
    # populate_database()
    # print_data("")