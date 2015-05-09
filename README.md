[![Build Status](https://travis-ci.org/wayeast/djangochallenge.svg?branch=master)](https://travis-ci.org/wayeast/djangochallenge)
Installation
===============
This project depends upon the virtualenv package
(`python-virtualenv` on Ubuntu).

Clone repo and `cd djangochallenge`.

Build
===============
`make cheeseshop` creates a virtual environment in a directory
`env` as well as a `log` directory.

Run
===============
`make run` starts a web server running on the local machine.
Point your browser to "localhost:8000" or "localhost:8000/arabic2roman"
to access the converter.

Test
===============
`make test` runs the project's built-in unit test framework.  This
consists of one test that tests the edge cases given in the
challenge writeup.

Cleanup
===============
`make clean` removes the virtualenv `env` and `log` directories as well
as all Python object files.
