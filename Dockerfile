FROM fedora:latest

RUN mkdir /app && dnf install -y which python3 python3-pip python3-pandas python3-numpy python3-scipy && \
    pip3 install --upgrade pip pipenv

COPY Pipfile Pipfile.lock /app/

WORKDIR /app

RUN pipenv install --system --dev

EXPOSE 8888

CMD jupyter notebook --port 8888 --allow-root --ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.password=''
