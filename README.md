
# Scrape UC Berkeley's Course Catalog

Quick little project to scrape what UC Berkeley has up on its course catalog 
(http://guide.berkeley.edu/courses/)

## Basic Setup

1. Create your virtual environment (used Python 3.8)
    -  `conda create -n courses python=3.8`
2. Install packages
   - Could use pip: `pip install -r requirements.txt`
3. You're ready to roll!

## Pure conda Setup

Simply run `conda env create -f environment.yml` which should produce the same virtual environment setup seen above.

## Usage

### Scrape Data

`python scrape.py` to scrape each topic into separate file (CSV)

Enjoy! 🤌🏼 


### Download Cached Data - (Previously scraped)

If you scraped the data and store it somewhere as a zip, use the `download.py` script.

```sh
python download.py <URL> <EXTRACTION_DIR>
```

* `<URL>` is the URL to the zip file. If not given, a default cache from a GitHub release is used.
* `<EXTRACTION_DIR>` is the directory to extract the zip into. If not given, defaults to the current working directory.