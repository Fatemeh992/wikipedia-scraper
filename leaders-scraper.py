import re
import requests
import time
import json
from bs4 import BeautifulSoup

def get_first_paragraph(wikipedia_url, session = None):
    if session is None:
        session = requests.Session()  
    soup = BeautifulSoup(session.get(wikipedia_url).text, "html.parser")
    paragraphs = [p for p in soup.select("#mw-content-text > div.mw-parser-output > p")]
    first_paragraph = None
    for p in paragraphs:
        if not p.has_attr("class"):
            first_paragraph = p
            break
    cleaned_text = re.sub(r'<[^>]+>|\[.*?\]|\(/.*?\)|\s+', ' ', first_paragraph.text).strip()
    return cleaned_text

def get_leaders():
    root_url = 'https://country-leaders.onrender.com'
    cookie_url = root_url + '/cookie'
    countries_url = root_url + '/countries'
    leaders_url = root_url + '/leaders'
    with requests.Session() as session:
        cookie = session.get(cookie_url)
        if cookie is not None and cookie.status_code == 200:
            headers = {"Cookie": cookie.headers['Set-Cookie']}
            countries = session.get(countries_url, headers = headers)
            if countries is not None and countries.status_code == 200:
                leaders_per_country = {country: session.get(leaders_url, headers=headers, params ={"country": country}).json() for country in countries.json()}        
                for _, leaders in leaders_per_country.items():
                    for leader in leaders:
                        wikipedia_url = leader['wikipedia_url']
                        leader["first_paragraph"] = get_first_paragraph(wikipedia_url, session)
                        time.sleep(0.2)

    return leaders_per_country

with open('leaders.json', 'w', encoding='utf-8') as f:
    leaders_per_country = get_leaders()
    json.dump(leaders_per_country, f)

# def save(leaders_per_country):
#     with open('leaders.json', 'r', encoding='utf-8') as f:
#         print(json.load(f))
