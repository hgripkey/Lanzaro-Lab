import urllib
import requests
from bs4 import BeautifulSoup
import re
import sys






#Web Scraper for lat and long of a location 
def make_URL(location):
    query = f"{location} latitude and longitude"
    query = query.replace(' ','+')
    URL = f"https://google.com/search?q={query}"

    return URL

def get_lat_long(soup):
    temp_str = str(soup.find('div',text = re.compile(DEGREE)))
    text = ""
    DEGREE = "° "
    for spl in re.split("<div|>|</div",temp_str):
        if DEGREE in spl:
            text = spl
    if text == "":
        print(f"Cannot find Degree symbol {DEGREE} on web page")
    else:
        text = text.split(', ')
        #Change to float values, and make S,W negative 
        if "S" in text[0]:
            text[0] = "-"+text[0]
        if "W" in text[1]:
            text[1] = "-"+text[1]
        text[0] = float(text[0].split(DEGREE)[0])
        text[1] = float(text[1].split(DEGREE)[0])
        return text
        