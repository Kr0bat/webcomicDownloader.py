import downloader, threading, os, time
from pathlib import Path


def downloadLovenstein():
    try:
        downloader.lovenstein()
    except FileExistsError:
        print("You already have the latest Lovenstein comic downloaded")

def downloadXkcd():
    try:
        downloader.xkcd()
    except FileExistsError:
        print("You already have the latest XKCD comic downloaded")
    

xkcdThread = threading.Thread(target=downloadXkcd)
lovensteinThread = threading.Thread(target=downloadLovenstein)

if not Path(r'.\Lovenstein').is_dir():
        Path(r'.\Lovenstein').mkdir()
if not Path(r'.\XKCD').is_dir():
        Path(r'.\XKCD').mkdir()
    

xkcdThread.start()
lovensteinThread.start()