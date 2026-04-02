from fetcher import fetch
from fetcher import parse
webContent=fetch("https://en.wikipedia.org/wiki/Python_(programming_language)")
if(not webContent):
    print("Unable to find the content")
else:
    title,text=parse(webContent)
    print("Title:",title)
    print("Text:",text)
    
