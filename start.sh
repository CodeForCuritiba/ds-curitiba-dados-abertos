#!/bin/bash

figlet "CODE4CWB"
echo "Starting Curitiba Dados abertos!";

# Instalando bibliotecas
pip install --upgrade requests pandarallel jupyterthemes;

# Instalando libs extras via PIP
pip install git+https://github.com/kavgan/word_cloud.git

figlet "Jupyter Start";

# Ativando extensões extras do jupyter
jupyter nbextension enable --py --sys-prefix qgrid;
jupyter nbextension enable --py --sys-prefix widgetsnbextension;

figlet "Jupyter Notebook";

# Customizando Jupyter Notebook - https://github.com/dunovank/jupyter-themes
jt -fs 95 -altp -tfs 11 -nfs 115 -cellw 94% -T

# Iniciando Jupyter Notebook
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token='' --NotebookApp.password='';
