[![Build Status](https://travis-ci.org/wayeast/djangochallenge.svg?branch=master)](https://travis-ci.org/wayeast/djangochallenge)

A web service that takes a base-ten number between 1 and 3999 as
form input data and displays it as a Roman numeral.  Uses a Gunicorn
web server in front of a Flask WSGI app.  By way of explanation for
why a project entitled 'Djangochallenge' does not use Django, Django
is a web app framework for building apps that run on top of
relational databases.  This project is a web app, but does not
require a database backend.  Hence, Flask is perfectly suitable for
it.

Installation
===============
System requirements
--------------------
This project requires the virtualenv package
(`python-virtualenv` on Ubuntu) to create an isolated
environment for the project.

Clone repo and `cd djangochallenge`.

Build
===============
`make cheeseshop` creates a virtual environment in a directory
`env` as well as a `log` directory in the project root.

Run
===============
`make run` starts a Gunicorn web server running on the local machine.
Point your browser to "localhost:8000" or "localhost:8000/arabic2roman"
to access the converter.

Test
===============
`make test` runs the project's built-in unit test framework.  This
consists of one test that tests the edge cases given in the
challenge writeup.  Note that this tests the logic of the Flask
routines, not the health of the Gunicorn -> Flask stack.

Cleanup
===============
`make clean` removes the virtualenv `env` and `log` directories as well
as all Python object files.
