from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import conf
from flask_cache import Cache  

conf_options = {
    "dev": "conf.DevConfig",
    "test1": "conf.Test1Config",
    "test2": "conf.Test2Config",
    "prod": "conf.ProdConfig"
}

def configure_app(conf = "dev"):
    app.config.from_object(conf_options[conf])

# general setup
app = Flask(__name__)
app.cache = Cache(app, config={'CACHE_TYPE': 'simple'})
db = SQLAlchemy(app)
# configure_app("prod")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

from app import models, views