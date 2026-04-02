import requests
from bs4 import BeautifulSoup
def fetch(url):
    # fetch the content of the url

    try:
        response=requests.get(url)
        return response.text
    except Exception as e:   
        print(e)
        return "Unable to fetch the url"    

def parse(html):
    #parse the content and find out the title,body and head
    soup=BeautifulSoup(html,"html.parser")
    title=soup.find("title").text
    head=soup.find("head").text
    body=soup.find("body").text
    return title,head,body
