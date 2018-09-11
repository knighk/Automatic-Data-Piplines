import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import time
import random

dfData=pd.read_csv("OCIS membership as per 4-22-2018.csv")
errorList=[]

for index, row in dfData.iterrows():
    print(index)
    randomNum=random.randrange(1,100)
    time.sleep(randomNum)
    if str(row["EMAIL"])!="nan":
        str1,str2=str(row["EMAIL"]).split("@")
        # try:
        url="https://scholar.google.com/scholar?hl=zh-TW&as_sdt=0%2C11&as_ylo=2017&q="+str1+"%40"+str2+"&btnG="

        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

        headers={'User-Agent':user_agent,}

        request=urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response,'html.parser')

        if soup.findAll("div",{"class":"gs_r gs_or gs_scl"}):
            resultList=soup.findAll("div",{"class":"gs_r gs_or gs_scl"})
            count=len(resultList)
            # row["count"]=count
            dfData.iloc[index,5]=count
            for index2, result in enumerate(resultList):
                head=result.find("a").get_text()
                link=result.find("a")['href']
                strHead="h"+str(index)
                strLink="l"+str(result)
                # row[strHead]=head
                # row[strLink] = link
                dfData.iloc[index,6+index2]=head
                dfData.iloc[index,7+index2]=link
                print(head)
                # print(link)
        else:
            # row["count"]=0
            dfData.iloc[index,5]=0
        # except:
        #     print(index)
        #     pass

dfData.to_csv("result.csv")