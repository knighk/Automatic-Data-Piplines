import pandas as pd
import numpy as np
import requests
import io
import urllib.request
from bs4 import BeautifulSoup as bs
import time
from random import randint

dfResult=pd.DataFrame(index=None,columns=["repository_name","repository_url","presository_description","labels","language","StarNum"])
# page=1
#
# url = "https://github.com/search?p=%s&q=CRM&type=Repositories" % (page)
# repositoryBaseUrl="https://github.com"
# result = urllib.request.urlopen(url)
# result = result.read()
# soup = bs(result, "lxml")
#
# # get whole content page
# si = soup.find("ul", {"class": "repo-list"})
#
# # get total page
# pageSoup=soup.find("div",{"class":"pagination"}).findAll("a")[-2]
# totalPage=int(pageSoup.text)
totalPage=50

############# temperature variables
# totalPage=2
# i=0

# loop into each page
for i in range(0,totalPage):
    page=i+1
    url = "https://github.com/search?p=%s&q=CRM&type=Repositories" % (page)
    repositoryBaseUrl = "https://github.com"
    time.sleep(randint(5, 10))
    result = urllib.request.urlopen(url)
    result = result.read()
    soup = bs(result, "lxml").find("body")

    #get repository list
    repoSoupList=soup.findAll("div",{"class":"repo-list-item d-flex flex-column flex-md-row flex-justify-start py-4 public source"})
    print("Page"+str(page))

    ##########
    # repoSoupList=repoSoupList[:1]

    for repoSoup in repoSoupList:
        repositoryNameSoup=repoSoup.find("a",{"class":"v-align-middle"})
        repositoryName=repositoryNameSoup.text
        repositoryUrl=repositoryNameSoup.get('href')
        repositoryUrl=repositoryBaseUrl+repositoryUrl

        # repository description
        repositoryDescriptionSoup=repoSoup.find("p",{"class":"col-12 col-md-9 d-inline-block text-gray mb-2 pr-4"})
        if repositoryDescriptionSoup:
            repositoryDescription=repositoryDescriptionSoup.text.split("\n")[1].strip()
        else:
            repositoryDescription=""

        # repository labels
        repositoryLabelSoupZone=repoSoup.find("div",{"class":"topics-row-container col-12 col-md-9 d-inline-flex flex-wrap flex-items-center f6 my-1"})
        repositoryLables = ""
        if repositoryLabelSoupZone:
            repositoryLabelSoupList=repositoryLabelSoupZone.findAll("a")
            for repositoryLabelSoup in repositoryLabelSoupList:
                repositoryLables+=repositoryLabelSoup.text

        # repository language and stars
        repositoryLanguageSoupZone=repoSoup.find("div",{"class","flex-shrink-0 col-6 col-md-4 pt-2 pr-md-3 d-flex"})
        repositoryLanguage=""
        reposirotyStar=""
        if repositoryLanguageSoupZone:
            repositoryLanguageSoup=repositoryLanguageSoupZone.find("div",{"class":"text-gray flex-auto min-width-0"})
            if repositoryLanguageSoup:
                repositoryLanguage=repositoryLanguageSoup.text
            repositoryStarSoup=repositoryLanguageSoupZone.find("a",{"class":"muted-link"})
            if repositoryStarSoup:
                repositoryStar=repositoryStarSoup.text
                # string with k to int
                # if "k" in repositoryStar:
                #     repositoryStar=float(repositoryStar.split("k")[0])*1000

        dfResult=dfResult.append({"repository_name":repositoryName,"repository_url":repositoryUrl,"presository_description":repositoryDescription,"labels":repositoryLables,"language":repositoryLanguage,"StarNum":repositoryStar},ignore_index=True)
        # time.sleep(randint(10, 15))

    if i%10==0:
        dfResult.to_csv("data\\resultTemp"+str(i)+".csv")

dfResult.to_csv("data\\result2_repositoryListPage_cluster.csv")