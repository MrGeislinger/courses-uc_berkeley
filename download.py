#!/usr/bin/python
# Downloads a cache of the scraped data from a URL
import sys
import urllib.request
import zipfile
from typing import Optional

def download_data(url: Optional[str], extract_dir: Optional[str]):
    '''
    '''
    if url is None:
        url = 'https://github.com/MrGeislinger/courses-uc_berkeley/releases/download/v1.0/courses_csv.zip'
        print(f'Using the default URL:\n\t{url}')
    # Note if extract_dir is None, will use current directory
    zip_path, _ = urllib.request.urlretrieve(url)
    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(extract_dir)

if __name__ == '__main__':
    # First argument is the URL but will use default cache if not given
    data_url = None
    try:
        data_url = sys.argv[1]
    except:
        print('You didn\'t specify the URL for the zip file')
    # Setting default extract directory (current working directory)
    extract_dir = None
    try:
        extract_dir = sys.argv[2]
    except:
        print('No extract directory specified. Using current directory.')

    download_data(data_url, extract_dir)