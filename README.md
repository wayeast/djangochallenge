DjangoChallenge
===============
[![Build Status](https://travis-ci.org/wayeast/djangochallenge.svg?branch=master)](https://travis-ci.org/wayeast/djangochallenge)

Installation
============
System Requirements
-------------------
This package depends upon Python virtualenv (python-virtualenv on Ubuntu
systems) and SQLite (sqlite3 on Ubuntu systems).

Build
=====
`make cheeseshop` creates a virtual environment in a directory `env` as well
as a `log` directory in the project root.

Run
===
`make [run]` starts a Gunicorn web server running on the local machine. Point
your browser to "localhost:8000" or "localhost:8000/arabic2roman" to access
the converter.

Test
====
`make test` runs the Django built-in test framework. This consists of one test
that tests the edge cases given in the challenge writeup, one that tests csrf_enforcement,
and one that tests responses to invalid input.

Cleanup
=======
`make clean` removes the virtualenv `env` and `log` directories as well as
all Python object files.
