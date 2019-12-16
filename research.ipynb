{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Curitiba - Base do 156"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import qgrid\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "from curitiba156 import get_downloaded_base156"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fetching latest base of 156...\n",
      "Latest csv url: http://dadosabertos.c3sl.ufpr.br/curitiba/156/2019-12-01_156_-_Base_de_Dados.csv\n",
      "Downloading File...\n",
      "File Already exists!\n",
      "No download needed.\n",
      "File source_data/base156.csv; Encoding: ISO-8859-1\n"
     ]
    }
   ],
   "source": [
    "csv_file, csv_encoding = get_downloaded_base156()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "field_names = ['SOLICITACAO', 'TIPO', 'ORGAO', 'DATA',\n",
    "               'HORARIO', 'ASSUNTO', 'SUBDIVISAO', 'DESCRICAO',\n",
    "               'LOGRADOURO_ASS', 'BAIRRO_ASS', 'REGIONAL_ASS',\n",
    "               'MEIO_RESPOSTA', 'OBSERVACAO', 'SEXO', 'BAIRRO_CIDADAO',\n",
    "               'REGIONAL_CIDADAO', 'DATA_NASC', 'TIPO_CIDADAO',\n",
    "               'ORGAO_RESP', 'RESPOSTA_FINAL', 'RESPOSTA_FINAL_DETALHE']\n",
    "\n",
    "data = pd.read_csv(csv_file, sep=';', encoding=csv_encoding, error_bad_lines=False, skiprows=[0,1], names=field_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b964a58514f848fea144a7551fc04951",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "QgridWidget(grid_options={'fullWidthRows': True, 'syncColumnCellResize': True, 'forceFitColumns': True, 'defau…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "qgrid.show_grid(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3d97fd70280f41fa88558752d468380e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "QgridWidget(grid_options={'fullWidthRows': True, 'syncColumnCellResize': True, 'forceFitColumns': True, 'defau…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_counts = data[['ORGAO']].groupby(['ORGAO']).size().reset_index(name='counts')\n",
    "qgrid.show_grid(data_counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.to_feather(fname='clean_data/data_processed.feather')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
