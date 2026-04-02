import requests
from bs4 import BeautifulSoup
def fetch(url):
    """fetch the content of the url"""
    #set a user-agent to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response=requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:   
        print(e)
        return None    

def parse(html):

    soup=BeautifulSoup(html,"html.parser")
    #remove the noise elements first
    for tag in soup(["script","style","meta","link"]):
        tag.decompose()
    #elements to focus on
    title=soup.find("title").get_text(strip=True) if soup.find("title") else ""
    main=(
        soup.find("main") or 
        soup.find("article") or 
        soup.find(id="content") or 
        soup.find(id="main-content") or
        soup.find("body")
    )
    #extract the clean text
    if(not main):
        return None, None
    text=main.get_text(separator=" ",strip=True)
    if (not text):
        print("Unable to extract meaningful text from the page")
    return title, text

