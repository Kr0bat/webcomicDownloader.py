# downloader.py
# Provides methods for downloading webcomics
# If the download fails, I should go on to the next one and try again later
import requests, bs4, re, time
from pathlib import Path

def xkcd():
    siteURL = "https://xkcd.com"
    site = requests.get(siteURL)
    site.raise_for_status()
    siteHTML = bs4.BeautifulSoup(site.text, 'html.parser')
    imageURL = siteHTML.select('meta[property="og:image"]')[0].get('content')
    title = siteHTML.select('meta[property="og:title"]')[0].get('content')
    title = f'{title}{Path(imageURL).suffix}'
    
    if (Path('XKCD') / title).is_file():
        raise FileExistsError
    
    image = requests.get(imageURL)
    image.raise_for_status()
    imageFile = open(Path('XKCD') / title, 'wb')
    
    for chunk in image.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    
def lovenstein():
    nameFormat = re.compile(r'Mr. Lovenstein \| ')
    siteURL = "https://www.mrlovenstein.com"
    site = requests.get(siteURL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"})
    site.raise_for_status()
    siteHTML = bs4.BeautifulSoup(site.text, 'html.parser')
    imageURL = siteURL + siteHTML.select('div > img')[0].get('src')
    title =  siteHTML.select('title')[0].text
    title = nameFormat.sub('', title)
    title = f'{title}{Path(imageURL).suffix}'
    
    if (Path('Lovenstein') / title).is_file():
        raise FileExistsError
    
    image = requests.get(imageURL)
    image.raise_for_status()
    imageFile = open(Path('Lovenstein') / title, 'wb')
    
    for chunk in image.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
