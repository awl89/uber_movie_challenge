from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from .models import MovieModel
from app import app, db
from flask import flash 
from forms import CreateMovieForm
from operator import itemgetter
import urllib2
import json
import time

'''
Helper functions
'''
def list_is_empty(l):
    return not l

def get_lat_lng(location):
    location_utf8 = urllib2.quote(location.encode("utf8"))
    print location_utf8
    request = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location_utf8 + ",+CA&key=" + app.config["API_KEY"]
    response = json.load(urllib2.urlopen(request))

    if response['status'] != "OK":
        return None

    coordinates = response['results'][0]['geometry']['location']
    lat = float(coordinates['lat'])
    lng = float(coordinates['lng'])

    print lat, lng
    return lat, lng
    
'''
Rounting functions
'''
@app.route('/')
def index():
    return render_template("index.html", API_KEY = app.config["API_KEY"])

@app.route('/search_title', methods=['GET'])
def search_title():
    search = request.args.get('title')
    movies = MovieModel.query.filter(MovieModel.title.ilike(search+'%')).all()
    if list_is_empty(movies):
        resp = jsonify({})
        resp.status_code = 404
        return resp
    else:
        res = [m.serialize() for m in movies]
        resp = jsonify(results = res)
        resp.status_code = 200
        return resp

@app.route('/create_movie', methods=['POST', 'GET'])
def create_movie():
    form = CreateMovieForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            lat_lng_result = get_lat_lng(form.location.data)
            if lat_lng_result is None:
                return render_template('create_movie.html', form=form, location_error=True)

            lat, lng = lat_lng_result
            movie = MovieModel( form.title.data,
                        int(form.year.data),
                        form.location.data,
                        form.fact.data,
                        form.company.data,
                        form.distributor.data,
                        form.director.data,
                        form.writer.data,
                        form.actor1.data,
                        form.actor2.data,
                        form.actor3.data,
                        float(lat),
                        float(lng))
            db.session.add(movie)
            db.session.commit()
            print "aaaaaaaaaaaaaaaaaa"
            return redirect('/')
            
    return render_template('create_movie.html', form=form, location_error = False)

@app.route('/list_movies')
@app.cache.cached(timeout=60) 
def list_movies():
    movies = MovieModel.query.all()
    movies_sorted = sorted(movies, key=lambda x: x.title)
    return render_template("list_movies.html", movies=movies_sorted)

'''
Simple view to proof that the cache actually works
'''
@app.route("/clock")
@app.cache.cached(timeout=300)  # cache this view for 5 minutes
def cached_view():
    return time.ctime()