import os

import requests

import pandas as pd

from xml.dom import minidom


def download_file(url, folder=None, name_override=None, force_overwrite=False):
    """ Downloads a file from a website

    params:
        - url (mandatory)
        - folder - Destination folder;
        - name_override - If provided, override the name of file,
                          if not pick latest part of url
        - force_overwrite - (bool) - Default False
    returns:
        - local_filename - The path of downloaded file
        - file_encoding
    """
    local_filename = url.split('/')[-1] if not name_override else name_override
    local_filename = local_filename if not folder \
        else f'{folder}/{local_filename}'

    print('Downloading File...')

    file_encoding = None
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        file_encoding = r.encoding

        if os.path.isfile(local_filename):
            print('File Already exists!')

            if not force_overwrite:
                print('No download needed.')
                return local_filename, file_encoding
            else:
                print('Forcing download anyway...')

        with open(local_filename, 'wb') as file_handler:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    file_handler.write(chunk)

    print('Download Sucessful')
    return local_filename, file_encoding


def get_latest_csv_url_from_156():
    """This fuction connects to website of dadosabertos, fetches and parses
    this file, collecting latest CSV.

    returns:
        - latest_csv_url - The full url of the latest CSV
    """
    print('Fetching latest base of 156...')

    base_url = 'http://dadosabertos.c3sl.ufpr.br/curitiba/156'

    xml_index_get_request = requests.get(f'{base_url}/156.xml')

    xml_index = None
    if xml_index_get_request.status_code == 200:
        xml_index = minidom.parseString(xml_index_get_request.text)
    else:
        raise SystemError('Unable to download database from Curitiba - 156')

    dados = xml_index.getElementsByTagName('dado')
    csv_file_url = None
    for dado in dados:
        name = dado.attributes['arquivo'].value
        if '.csv' in name:
            csv_file_url = name
            break

    latest_csv_url = f'{base_url}/{csv_file_url}'

    print(f'Latest csv url: {latest_csv_url}')

    return latest_csv_url


def get_downloaded_base156():
    """ Downloads the base156.

    returns:
        - csv_filename - The relative file location, on your filesystem
        - csv_filename_encoding
    """

    csv_url = get_latest_csv_url_from_156()
    csv_filename, csv_filename_encoding = \
        download_file(csv_url, folder='source_data',
                      name_override='base156.csv',
                      force_overwrite=False)

    print(f'File {csv_filename}; Encoding: {csv_filename_encoding}')

    return csv_filename, csv_filename_encoding


def main():
    csv_file, csv_encoding = get_downloaded_base156()


if __name__ == '__main__':
    main()
