DJ_PY=python manage.py
PIP=pip
VENV=./env/bin/activate


.PHONY: all \
	cheeseshop \
	clean

all: cheeseshop

cheeseshop:
	if [ ! -d ./env ] ; then \
		virtualenv env ; \
		. $(VENV) ; \
		$(PIP) install -r requirements.txt ; \
		deactivate ; \
	fi
	if [ ! -d ./log ] ; then \
		mkdir log ; \
	fi
	. $(VENV) && $(DJ_PY) migrate && deactivate

clean:
	if [ -d ./env ] ; then \
		rm -rf env ; \
	fi
	rm db.sqlite3
	rm -rf log
	find . -name *.pyc -delete
