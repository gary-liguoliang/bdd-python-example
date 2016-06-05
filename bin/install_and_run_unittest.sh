#!/usr/bin/env bash

virtualenv venv
. venv/bin/activate

pip install -r requirements.txt
pip install -e .

nosetests --with-xunit --with-coverage --cover-xml