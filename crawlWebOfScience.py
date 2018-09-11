from wos import WosClient
import wos.utils

with WosClient("", '') as client:
    print((wos.utils.query(client, 'AU=Goncalves, Renata AND PY=2017')))
    # print((wos.utils.query(client, 'TI=(GRONS: a comprehensive genetic resource of nicotine and smoking)')))
    # print((wos.utils.query(client, 'DOI=BUSH KAREN AND PY=(2015 AND 2016)')))