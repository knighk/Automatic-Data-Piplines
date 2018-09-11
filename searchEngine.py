import csv
import pandas as pd
import glob, os
import re

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

def hasFoundCompany(dfResult, str_file,fileCik,name1,nameListOriginal_i,confidence,line):
    for key in listSupplyChainKeywords:
        if key in line:
            dfResult = dfResult.append({"file": str_file,
                                        "cik": fileCik, "relatedSimplest": name1,
                                        "relatedOrigianl": nameListOriginal_i,"supplyKey":key, "confidence": confidence,"line": line},
                                       ignore_index=True)
    return dfResult

def checkline(dfResult,file,fileCik):
    with open(file, 'r') as inF:
        for line in nonblank_lines(inF):
            line=line.lower()
            flagFound=0
            for i, name2 in enumerate(nameListSimplest):
                name2=name2.lower()
                name1 =" "+name2+" "
                confidence=0;
                print(name1);

                if name1 in line:
                    print(name1+" in line")
                    flag=1
                    if fileCik == cikList[i]:
                        flagFound = 1
                        continue
                    lineList=line.split(" ")
                    keyLocation=lineList.index(name1.split(' ')[-2])
                    if len(lineList[keyLocation-1])!=0 and lineList[keyLocation-1][0].isupper():
                        print("tag1");
                        flag=0
                    if len(lineList[keyLocation-1])!=0 and (lineList[keyLocation-1] in excluedFrontList):
                        print("tag2");
                        flag=0
                    if flag==1:
                        print("tag3");
                        if nameListOriginal[i].lower() in line.lower():
                            confidence=2
                        elif len(name1)>2:
                            confidence=1
                        dfResult=hasFoundCompany(dfResult,str(file),fileCik,name1,nameListOriginal[i],confidence,line)
                        flagFound = 1
                        break
                else:
                    continue
            # if flagFound==0:
            #     if "(nyse" in line.lower():
            #         try:
            #             keyLocation = [i for i, s in enumerate(line.lower().split(" ")) if '(nyse:' in s]
            #             tag=line.split(" ")[keyLocation[0]]
            #         except:
            #             tag = "(nyse"
            #             confidence=1
            #             dfResult =hasFoundCompany(dfResult,str(file), ticker, companyName, fileCik, tag, tag, confidence,line)
            #             pass
            #     if "(nasdaq" in line.lower():
            #         try:
            #             keyLocation = [i for i, s in enumerate(line.lower().split(" ")) if '(nasdaq:' in s]
            #             tag=line.split(" ")[keyLocation[0]]
            #         except:
            #             tag = "(nasdaq"
            #             confidence=1
            #             dfResult =hasFoundCompany(dfResult,str(file), ticker, companyName, fileCik, tag, tag, confidence, line)
            #             pass
    return dfResult

path_d = 'F:\\fintech\\nine\\';
path_data='J:\\data\\edgar\\2016\\temp\\';

rootDir = os.getcwd()  # save our current directory
df=pd.read_csv("nameList.csv")
listSupplyChainKeywords=pd.read_csv("supplyChainKeys.csv")["keys"].tolist()
nameListOriginal = df["conm"].tolist()
nameListSimplest = df["nameSimplest"].tolist()
cikList = df["cik"].tolist()
excluedList0 = ["city","agency"]
excluedFrontList = ["said","stated"]
dfResult=pd.DataFrame(index=None,columns=["file","cik","relatedSimplest","relatedOrigianl","confidence","supplyKey","line"])
n=0

os.chdir(path_data+"txt")
for file in glob.glob("*.txt"):
    if '_8-K_' not in str(file):
        continue
    n=n+1

    if n%1000==0:
        fileName="searchTXTLarger_result_test"+str(n)+".csv"
        dfResult.to_csv(os.path.join(path_d, fileName))
        #break

    fileCik=int(str(file).split('_')[0])
    print(file)

    if any(df["cik"] == fileCik):
        index = df.index[df['cik'] == fileCik].tolist()[0]
        cik=df.get_value(index, 'cik')
    else:
        index = "No Match"
        cik="No Match"

    dfResult=checkline(dfResult,file,fileCik)

dfResult.to_csv("F:\\fintech\\nine\\result\\searchTXTLarger_result.csv",encoding="utf-8")

