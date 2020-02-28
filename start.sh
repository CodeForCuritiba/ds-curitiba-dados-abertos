#!/bin/bash

figlet "CODE FOR CURITIBA"
echo "Iniciando painel dados abertos";

# Instalando bibliotecas
figlet "Pacotes Python..."
pip install --upgrade pip;
pip install notebook jupyter_contrib_nbextensions requests pandarallel jupyterthemes curitiba-dados-abertos;
pip install jupyter_nbextensions_configurator;

figlet "Pacotes Jupyter...";

# Ativando extensões extras do jupyter
jupyter contrib nbextension install --sys-prefix;
jupyter nbextensions_configurator enable --sys-prefix
jupyter nbextension enable --py --sys-prefix qgrid;
jupyter nbextension enable --py --sys-prefix widgetsnbextension;
jupyter nbextension enable --sys-prefix hinterland/hinterland;
jupyter nbextension enable --sys-prefix scroll_down;
jupyter nbextension enable --sys-prefix gist_it/main;
jupyter nbextension enable --sys-prefix execute_time/ExecuteTime;
jupyter nbextension enable --sys-prefix "tree-filter/index";


figlet "Iniciando Jupyter";
echo "Carregando serviço na porta 8888"
# Customizando Jupyter Notebook - https://github.com/dunovank/jupyter-themes
jt -fs 95 -altp -tfs 11 -nfs 115 -cellw 94% -T

# Iniciando Jupyter Notebook
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token='' --NotebookApp.password='';
