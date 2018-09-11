import pandas as pd
import numpy as np
import requests
import io
import urllib.request
from bs4 import BeautifulSoup
import csv

urlPool=[
"http://zipatlas.com/us/ga/zip-code-comparison/male-to-female-ratio.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/female-to-male-ratio.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/population-density.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/median-age.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-children.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-seniors.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-white-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-black-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-native-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-asian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-indian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-chinese-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-filipino-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-japanese-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-korean-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-hispanic-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-mexican-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-cuban-population.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-high-school-students.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-college-students.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-high-school-graduates.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-college-graduates.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-arab-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-czech-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-danish-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-dutch-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-english-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-french-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-french-canadian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-german-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-greek-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-hungarian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-irish-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-italian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-lithuanian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-norwegian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-polish-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-portuguese-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-russian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-scottish-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-slovak-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-swedish-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-swiss-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-ukrainian-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-welsh-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-west-indian-population.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-in-labor-force.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-males-in-labor-force.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-females-in-labor-force.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-military-population.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-not-in-labor-force.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-government-employees.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-self-employed.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/unemployment-rate.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-professional-jobs.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-service-jobs.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-sales.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-farming-jobs.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-construction-jobs.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-production-transportation-jobs.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-agriculture-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-construction-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-manufacturing-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-retail-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-transportation-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-information-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-finance-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-professional-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-education-social-services-industry.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-arts-entertainment-industry.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-income-under-10k.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-income-over-100k.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-income-over-200k.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/median-household-income.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/average-income-per-person.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/population-below-poverty-level.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/families-below-poverty-level.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-work-at-home.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-walk-to-work.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-take-public-transit-to-work.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-drive-to-work.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-population-carpooling-to-work.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/average-commute-time.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-housing-units-occupied-by-owner.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-housing-units-occupied-by-renter.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-vacant-housing-units.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-detached-homes.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-apartment-buildings.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/average-number-rooms.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-utility-gas-heating.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-bottled-gas-heating.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-electricity-heating.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-fuel-oil-heating.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-coal-heating.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-wood-heating.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-solar-heating.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-properties-under-200000.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-properties-under-500000.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-properties-over-500000.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-properties-over-1-million.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-properties-without-mortgage.htm",

"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-one-or-more-vehicles.htm",
"http://zipatlas.com/us/ga/zip-code-comparison/percentage-households-two-or-more-vehicles.htm"]

for urlRaw in urlPool:
    urlBase=urlRaw.split(".htm")[0]
    print(urlBase)
# urlBase = "http://zipatlas.com/us/ga/zip-code-comparison/male-to-female-ratio"
    fileName=urlBase.split("/")[-1]+".csv"
    url=urlBase+".htm"
    result = urllib.request.urlopen(url)
    result = result.read()
    soup = BeautifulSoup(result, "lxml")
    si = soup.find("table", {"rules": "all"})
    dfResult = pd.read_html(str(si))[0]

    n=2
    while True:
        print(n)
        urlTemp=urlBase+"."+str(n)+".htm"
        result = urllib.request.urlopen(urlTemp)
        result = result.read()
        soup = BeautifulSoup(result,"lxml")
        si = soup.find("table", {"rules": "all"})
        df1 = pd.read_html(str(si))[0]
        if df1.shape[0]==1:
            break
        dfResult=pd.concat([dfResult,df1[1:]],axis=0)
        n+=1
        # break

    dfResult[dfResult.columns[1:]].to_csv(fileName,header=None,index=None)

