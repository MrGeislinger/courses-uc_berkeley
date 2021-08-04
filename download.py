#!/usr/bin/python
# Downloads a cache of the scraped data from a URL
import sys
import urllib.request
import zipfile

# First argument is the URL but will use default cache if not given
url = 'https://github.com/MrGeislinger/courses-uc_berkeley/releases/download/v1.0/courses_csv.zip'
try:
    url = sys.argv[1]
except:
    print('You need to specify the URL for the zip file')
    
    print(f'Using the default cache:\n\t{url}')

# Setting default extract directory (current working directory)
extract_dir = None
try:
    extract_dir = sys.argv[2]
except:
    print('No extract directory specified. Using current directory.')

zip_path, _ = urllib.request.urlretrieve(url)
with zipfile.ZipFile(zip_path, "r") as f:
    f.extractall(extract_dir)