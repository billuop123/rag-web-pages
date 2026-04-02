from fetcher import fetch
from fetcher import parse
webContent=fetch("https://www.google.com")
if(not webContent):
    print("Unable to find the content")
if (webContent): 
    head,title,body=parse(webContent)
    print("Head:",head)
    print("Title:",title)
    print("Body:",body)
    if (not head and not title and  not body):
        print("Unable to parse the content")
