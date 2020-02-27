#!/bin/bash

figlet "CODE FOR CURITIBA"
echo "Iniciando painel dados abertos";

# Instalando bibliotecas
figlet "Pacotes Python..."
pip install --upgrade pip;
pip install --upgrade requests pandarallel jupyterthemes curitiba-dados-abertos;

figlet "Pacotes Jupyter...";

# Ativando extensões extras do jupyter
jupyter nbextension enable --py --sys-prefix qgrid;
jupyter nbextension enable --py --sys-prefix widgetsnbextension;

figlet "Iniciando Jupyter";
echo "Carregando serviço na porta 8888"
# Customizando Jupyter Notebook - https://github.com/dunovank/jupyter-themes
jt -fs 95 -altp -tfs 11 -nfs 115 -cellw 94% -T

# Iniciando Jupyter Notebook
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token='' --NotebookApp.password='';
