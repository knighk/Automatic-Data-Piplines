import pandas_datareader.data as web
import pandas as pd
import datetime
import csv

def get_price_and_volume(symbol):
    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime(2017, 9, 25)
    f = web.DataReader( symbol,'yahoo', start, end)
    df=pd.DataFrame(f)
    df.reset_index()
    return df

failList=[];
with open('kSymbolk.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

for i in range(0,len(data_read)):
    symbol = data_read[i][0]
    name=str('data/'+symbol+'.csv')
    try:
        df = get_price_and_volume(symbol)
        df.to_csv(name,mode = 'w', encoding='utf-8')
    except:
        failList.append(symbol)
        pass

thefile = open('data/failed.txt', 'w')
for item in failList:
    thefile.write("%s\n" % item)


#print(df)
