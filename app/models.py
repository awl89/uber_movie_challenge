from app import db

class MovieModel(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True)
    year = db.Column(db.Integer)
    location = db.Column(db.String(128))
    fact = db.Column(db.String(512))
    company = db.Column(db.String(80))
    distributor = db.Column(db.String(80))
    director = db.Column(db.String(80))
    writer = db.Column(db.String(80))
    actor1 = db.Column(db.String(80))
    actor2 = db.Column(db.String(80))
    actor3 = db.Column(db.String(80))
    lng = db.Column(db.Float())
    lat = db.Column(db.Float())

    def __init__(self, title, year, location, fact, company, distributor, \
                director, writer, actor1, actor2, actor3, lng, lat):
        self.title = title
        self.year = year
        self.location = location
        self.fact = fact
        self.company = company
        self.distributor = distributor
        self.director = director
        self.writer = writer
        self.actor1 = actor1
        self.actor2 = actor2
        self.actor3 = actor3
        self.lng = lng
        self.lat = lat

    def serialize(self):
        return {
                'title': self.title,
                'year': self.year,
                'location': self.location,
                'fact': self.fact,
                'company': self.company,
                'distributor': self.distributor,
                'director': self.director,
                'writer': self.writer,
                'actor1': self.actor1,
                'actor2': self.actor2,
                'actor3': self.actor3,
                'lng': self.lng,
                'lat': self.lat
            }