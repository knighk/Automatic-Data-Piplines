import pandas as pd
import urllib.request
from bs4 import BeautifulSoup as bs
import time
from random import randint

dfRepositoryUrlList=pd.read_csv("repositoryUrlList_test.csv")["repository_url"].tolist()
dfResultRepository=pd.DataFrame(index=None,columns=["repository_url","watch","star","fork","open","closed"])
dfResultOpenPulls=pd.DataFrame(index=None,columns=["repository_url","open_pull_url","titles","discuss","description","process"])

for i in range(0, len(dfRepositoryUrlList)):
    repositoryUrl=dfRepositoryUrlList[i]+"/pulls?q=is%3Aopen+is%3Apr"
    time.sleep(randint(5, 10))
    result = urllib.request.urlopen(repositoryUrl)
    result = result.read()
    soup = bs(result, "lxml").find("body")

    # watch, star, fork
    WSF=["","",""]
    zoneSoup=soup.find("ul",{"class":"pagehead-actions"}).findAll("li")
    for i in range(0,len(zoneSoup)):
        zoneSoup2=zoneSoup[i].findAll("a")[-1]
        WSF[i]=zoneSoup2.text.split("\n")[1].strip()

    # open, closed number
    open=""
    closed=""
    zoneSoup=soup.find("a",{"class":"btn-link selected"})
    if zoneSoup:
        open=zoneSoup.text.split("Open")[0].strip()
    zoneSoup=soup.find("a",{"class":"btn-link "})
    if zoneSoup:
        closed=zoneSoup.text.split("Closed")[0].strip()

    dfResult = dfResultRepository.append({"repository_url":dfRepositoryUrlList[i],"watch":WSF[0],"star":WSF[1],"fork"WSF[2],"open":open,"closed":closed}, ignore_index=True)

    # get total pages
    zoneSoup=soup.find("div",{"class":"pagination"})
    pages=1
    if zoneSoup:
        pagesSoup=zoneSoup.findAll("a")
        pages=int(pagesSoup[-2].text)
    https: // github.com / salesagility / SuiteCRM / pulls


    # open pulls
    zoneSoup=soup.find("ul",{"class":"js-navigation-container js-active-navigation-container"})
    if zoneSoup:
        openSoupList=zoneSoup.findAll("li")
        for i in range(0,len(openSoupList)):
