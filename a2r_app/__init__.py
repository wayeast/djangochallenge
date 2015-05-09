# flake8: noqa
from flask import Flask

from a2r_number import Arabic2Roman

app = Flask('a2r_app')
app.config.from_object('config')

from a2r_app import views
