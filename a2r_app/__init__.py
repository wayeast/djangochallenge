from flask import Flask

app = Flask('a2r_app')
app.config.from_object('config')

from a2r_app import views
