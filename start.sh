#!/bin/bash

figlet "CODE4CWB"
echo "Starting Curitiba Dados abertos!";
rm requirements*.txt;
pipenv_to_requirements;
pip install -r requirements.txt

figlet "Init Jupyter"
jupyter notebook --port 8888 --allow-root --ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.password=''
