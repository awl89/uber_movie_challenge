from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms import validators


class CreateMovieForm(Form):
    title = StringField('Title', validators=[validators.DataRequired(), validators.Length(min=2, max=50)], default="Title")
    year = IntegerField('Year', validators=[validators.DataRequired()], default="Year")
    location = StringField('Location', validators=[validators.DataRequired()], default="Location")
    fact = StringField('Fact', default="Fact")
    company = StringField('Company', default="Company")
    distributor = StringField('Distributor', default="Distributor")
    director = StringField('Director', validators=[validators.DataRequired()], default="Director")
    writer = StringField('Writer', default="Writer")
    actor1 = StringField('Actor1', default="Actor 1")
    actor2 = StringField('Actor2', default="Actor 2")
    actor3 = StringField('Actor3', default="Actor 3")