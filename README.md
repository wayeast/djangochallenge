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

Cleanup
=======
`make clean` removes the virtualenv `env` and `log` directories as well as
all Python object files.
