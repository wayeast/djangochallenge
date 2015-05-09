Installation
===============
This project depends upon the virtualenv package
(`python-virtualenv` on Ubuntu).

Unpack tarball and `cd djangochallenge`.

Build
===============
`make cheeseshop` creates a virtual environment in a directory
`env`.

Run
===============
`make run` starts a web server running on the local machine.
Point your browser to "localhost:5000" or "localhost:5000/arabic2roman"
to access the converter.

Test
===============
`make test` runs the project's built-in unit test framework.  This
consists of one test that tests the edge cases given in the
challenge writeup.

Cleanup
===============
`make clean` removes the virtualenv `env` directory and all python
object files.
