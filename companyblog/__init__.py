import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# Determine base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Use DATABASE_URL env variable if exists, else fallback to local SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# Blueprint registrations
from companyblog.core.views import core
from companyblog.error_pages.handlers import error_pages
from companyblog.users.views import users
from companyblog.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)
