# flake8: noqa
import os
import logging
from logging import FileHandler

from flask import Flask

app = Flask('a2r_app')
app.config.from_object('config')

# set app logging
logdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')
handler = FileHandler(os.path.join(logdir, 'a2r_app.log'), mode='w')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s - %(levelname)s] %(name)s: %(message)s')
handler.setFormatter(formatter)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)

from a2r_number import Arabic2Roman
from a2r_app import views
