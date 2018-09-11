# -*- coding: cp936 -*-
import requests
import csv

class Load_Corpus_with_Iteration(object):  
    def __init__(self, path):  
        self.path = path  
  
    def __iter__(self):  
        for line in open(self.path):  
            yield line.split()

corpus = Load_Corpus_with_Iteration('downList.txt')

for item in corpus:
    #print(item)
    name=item[0].split('/')
    #print(name[6])
    r = requests.get(item[0], stream=True)

    with open(name[6], 'wb') as fd:
        for chunk in r.iter_content(900000000):
            fd.write(chunk)
    print(item)
