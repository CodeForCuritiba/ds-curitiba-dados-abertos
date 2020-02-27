# Curitiba - Dados Abertos
## Arquivo limpo do dadosbertos - Portal curitiba.pr.gov.br

[![Build Status](https://travis-ci.org/CodeForCuritiba/ds-curitiba-dados-abertos.svg?branch=master)](https://travis-ci.org/CodeForCuritiba/ds-curitiba-dados-abertos)

Esse repositório visa abranger todos os dados do portal da transparência de maneira limpa e pronta para ser utilizada por programas de BI. [](https://www.curitiba.pr.gov.br/dadosabertos/busca/)
O mesmo gera entregáveis que podem ser acessados facilmente na aba "releases" deste mesmo repositório. Este é um projeto piloto do code for Curitiba que visa utilizar técnicas de CI/CD.

## Como acessar os dados
Esse projeto foi construído em cima do `docker-composer`. Este permite a criação de um ambiente pronto para funcionamento em todas as plataformas: Windows, Linux e Mac OS;
O instalador para Windows pode ser encontrado em [](https://docs.docker.com/docker-for-windows/).

## Instalação e primeiro acesso
Para instalar esse repositório, faça download dos arquivos ou clone este repositório GIT e, dentro do diretório dele, execute os seguintes comandos.

    docker-compose up -d

Aponte o navegador para `http://localhost:8888` e pronto! Você terá um sistema com o jupyter notebook instalado. [](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)

## Executando testes
Esse projeto foi composto de uma suíte de testes unitários. Estes servem para garantir a assertividade do projeto, assim como parâmetro de qualidade para o desenvolvimento de novas melhorias.
Para a execução dos testes, digite o seguinte comando:

    docker-compose exec jupyter pytest --cov=curitiba156

## Contribua!
Dúvidas? Está afim de contribuir? Por favor crie um issue nesse projeto!

## Mantenedor
Esse projeto está sendo inicialmente mantido por:

* Jon Trigueiro <joepreludian at gmail dot com>
