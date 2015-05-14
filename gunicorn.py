import os
import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
backlog = 2048
proc_name = 'a2r_gunicorn'

logdir = '/var/log/a2r'
errorlog = os.path.join(logdir, 'gunicorn_error.log')
accesslog = os.path.join(logdir, 'gunicorn_access.log')
loglevel = "info"
