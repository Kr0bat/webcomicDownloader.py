# downloader.py
# Provides methods for downloading webcomics
# This line is pointless
import requests, bs4
from os.path import basename
from pathlib import Path

def xkcd():
    siteURL = "https://xkcd.com"
    site = requests.get(siteURL)
    site.raise_for_status()
    siteHTML = bs4.BeautifulSoup(site.text, 'html.parser')
    imageURL = siteHTML.select('meta[property="og:image"]')[0].get('content')
    title = siteHTML.select('meta[property="og:title"]')[0].get('content')
    
    image = requests.get(imageURL)
    image.raise_for_status()
    imageFile = open(f'{title}{Path(imageURL).suffix}', 'wb')
    
    for chunk in image.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    
xkcd()

