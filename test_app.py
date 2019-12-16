import os

import pytest
from pathlib import Path

from curitiba156 import \
    get_downloaded_base156, get_latest_csv_url_from_156, download_file


@pytest.fixture
def supply_download_data():
    return {
        'url': 'https://www.google.com.br/intl/pt-BR/add_url.html',
        'temp_name': 'temp_name',
        'temp_dir': 'source_data'
    }


def test_get_url_156():
    url = get_latest_csv_url_from_156()

    assert 'Base_de_Dados.csv' in url
    # assert 'ISO-8859-1' in charset


def test_download_simple_file(supply_download_data):

    filename, encoding = download_file(url=supply_download_data['url'])

    assert filename == 'add_url.html'
    assert os.path.isfile(filename) is True

    os.unlink('add_url.html')  # Cleaning up file


def test_download_file_with_override(supply_download_data):

    filename, encoding = download_file(
        url=supply_download_data['url'],
        name_override=supply_download_data['temp_name'])

    assert filename == supply_download_data['temp_name']
    assert os.path.isfile(filename) is True

    os.unlink(filename)


def test_download_file_with_folder(supply_download_data):

    filename, encoding = download_file(
        url=supply_download_data['url'],
        folder=supply_download_data['temp_dir'])

    assert filename == f'{supply_download_data["temp_dir"]}/add_url.html'
    assert os.path.isfile(filename) is True

    os.unlink(filename)


def test_download_file_with_folder_and_name_override(supply_download_data):

    filename, encoding = download_file(
        url=supply_download_data['url'],
        folder=supply_download_data['temp_dir'],
        name_override=supply_download_data['temp_name'])

    assert filename == f'{supply_download_data["temp_dir"]}/' \
                       f'{supply_download_data["temp_name"]}'
    assert os.path.isfile(filename) is True

    os.unlink(filename)


def test_download_no_overwrite(supply_download_data):

    filename, encoding = download_file(
        url=supply_download_data['url'],
        folder=supply_download_data['temp_dir'],
        name_override=supply_download_data['temp_name'])

    assert filename == f'{supply_download_data["temp_dir"]}/' \
                       f'{supply_download_data["temp_name"]}'

    assert os.path.isfile(filename) is True

    Path(filename).touch()
    file_stats_touched = os.stat(filename)
    assert type(file_stats_touched.st_mtime) is float

    # Downloading again and comparises if the file was overwritten
    filename, encoding = download_file(
        url=supply_download_data['url'],
        folder=supply_download_data['temp_dir'],
        name_override=supply_download_data['temp_name'],
        force_overwrite=False)

    file_stats_new = os.stat(filename)
    assert file_stats_touched.st_mtime == file_stats_new.st_mtime

    os.unlink(filename)


def test_download_with_overwrite(supply_download_data):

    filename, encoding = download_file(
        url=supply_download_data['url'],
        folder=supply_download_data['temp_dir'],
        name_override=supply_download_data['temp_name'])

    assert filename == f'{supply_download_data["temp_dir"]}/' \
                       f'{supply_download_data["temp_name"]}'
    assert os.path.isfile(filename) is True

    Path(filename).touch()
    file_stats_touched = os.stat(filename)
    assert type(file_stats_touched.st_mtime) is float

    # Downloading again and comparises if the file was overwritten
    filename, encoding = download_file(
        url=supply_download_data['url'],
        folder=supply_download_data['temp_dir'],
        name_override=supply_download_data['temp_name'],
        force_overwrite=True)

    file_stats_new = os.stat(filename)
    assert file_stats_touched.st_mtime != file_stats_new.st_mtime

    os.unlink(filename)


def test_get_base156():
    filename, encoding = get_downloaded_base156()

    assert filename == 'source_data/base156.csv'
    assert os.path.isfile(filename)
