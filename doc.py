# -*- coding: cp936 -*-
import pandas
import numpy as np
import requests
import io
import urllib.request
from bs4 import BeautifulSoup as bs
import csv
 
def main():
    dlist=[]
    downLink=get_link()
    
    #for i in range(len(klist)):
    #    url=klist[i][0]
    #    downLink=get_link(url)
    #    dlist.append(downLink)
    #fd = open('downList.csv','a')
    #fd.write(downLink)
    #fd.close()

    #print(dlist)
    
        
def get_link():
    klist=[104516,
105041,
106289,
104976,
104543,
104587,
104590,
104600,
104614,
105190,
104630,
104645,
104654,
104657,
104674,
104502,
104710,
104723,
104711,
105086,
104771,
104796,
104802,
104812,
104817,
104833,
104838,
104865,
104905,
104884,
104934,
104975,
104954,
104967,
104972,
104976,
104981,
105011,
105012,
105007,
105015,
105324,
105021,
105041,
106175,
105714,
105060,
105953,
105832,
105083,
105085,
105086,
105089,
105094,
105138,
105152,
105144,
105160,
105172,
105173,
105181,
105187,
105190,
105878,
105199,
105233,
105222,
105226,
105266,
105324,
106283,
105283,
105287,
105306,
106100,
105341,
105820,
105342,
105349,
105369,
105600,
105714,
105377,
105599,
105609,
105817,
105624,
105705,
105632,
105637,
105650,
105660,
105681,
105720,
106105,
105724,
105664,
105712,
105737,
105947,
105757,
105819,
105766,
105820,
105822,
105795,
106157,
105803,
105812,
105832,
105968,
105857,
105858,
105972,
105875,
105878,
105877,
105895,
105897,
105904,
105908,
105911,
105939,
105952,
105947,
105953,
105986,
105992,
106003,
106004,
105936,
106023,
106106,
106108,
106105,
106166,
106194,
106211,
106221,
106235,
106258,
106259,
104965,
104557,
104609,
104810,
104822,
105353,
104946,
104991,
105022,
105097,
105112,
105132,
105205,
105275,
105353,
105362,
105363,
105628,
105629,
106133,
105701,
105703,
105763,
105776,
105884,
105948,
105994,
106031,
104568,
104629,
104658,
104780,
104798,
104809,
105090,
106261,
104970,
104821,
106028,
105207,
105239,
105345,
105372,
106262,
105689,
105623,
105870,
105869,
105896,
105921,
106013,
106085,
106035,
106152,
106199,
104806,
104855,
104973,
106185,
105039,
105119,
105220,
105251,
105750,
105764,
105843,
106185,
105159,
104585,
104728,
105110,
105322,
106256,
102317,
104538,
104595,
104749,
104821,
105019,
105054,
105062,
105147,
105167,
105169,
105235,
105248,
105290,
106107,
106285,
106321,
105721,
105730,
105739,
105751,
106131,
105790,
105827,
105829,
105914,
106139,
106119,
106054,
106111,
106107,
106073,
106076,
106079,
106135,
106315,
104597,
104577,
104843,
104948,
104961,
106067,
105084,
105176,
105302,
105597,
105684,
106005,
105974,
104591,
104513,
104745,
104755,
104739,
104742,
104683,
104794,
104808,
104956,
104895,
104968,
105136,
105107,
105277,
105221,
106146,
105296,
106272,
105343,
105591,
105704,
105613,
105715,
105635,
105985,
105781,
105977,
105733,
105958,
105783,
105889,
106067,
106151,
106294,
106309,
105840,
104570,
104738,
104907,
105351,
105254,
105665,
106050,
104582,
104556,
104618,
104849,
104534,
104549,
104559,
104574,
104580,
104593,
104826,
104716,
104811,
104839,
104847,
104987,
105051,
104889,
104929,
104987,
105134,
105025,
105026,
105051,
105988,
105134,
105170,
105183,
105270,
105326,
105331,
106202,
105598,
105611,
105638,
105758,
105802,
105853,
105871,
105887,
105938,
105951,
105988,
106103,
104581,
104846,
104640,
105956,
104935,
106255,
105241,
105285,
106317,
105941,
105975,
104641,
104842,
105058,
105997,
104767,
104917,
106007,
106148,
104520,
105002,
104644,
105826,
106202,
104566,
104915,
104344,
104621,
104634,
104680,
104746,
104751,
104754,
104863,
104876,
105115,
104908,
104940,
104957,
104974,
104992,
105023,
105954,
105045,
105099,
106124,
106087,
105067,
105880,
105174,
105295,
105262,
105374,
105589,
105590,
105646,
105706,
105659,
105673,
105680,
106124,
105745,
105748,
105768,
105791,
105831,
105833,
105967,
105873,
105880,
105899,
105909,
105954,
106075,
106083,
106087,
106032,
106038,
106088,
106043,
106124,
106143,
106253,
106266,
106270,
106278,
106295,
106303,
106304,
104663,
104759,
104806,
106079,
104860,
105654,
105691,
105859,
105907,
105910,
105981,
106041,
106191,
105273,
105738,
105845,
105836,
106015,
105937,
105959,
106096,
106220,
104517,
104589,
104647,
104721,
105072,
105850,
105850,
105072,
105135,
105250,
105348,
105594,
105699,
105804,
105850,
105903,
106084,
106183,
105940,
104786,
104788,
106252,
104836,
104882,
104924,
104964,
105101,
105940,
106080,
106203,
104575,
104715,
105201,
105979,
104692,
104822,
104845,
105234,
105339,
105814,
104820,
105841,
105834,
105929,
106131,
106065,
104544,
104881,
104931,
104953,
104877,
105010,
105818,
106251,
105279,
106227,
104722,
105289,
104527,
104558,
104665,
104685,
104702,
104736,
104774,
104911,
104904,
104851,
104848,
104911,
104944,
104947,
104990,
105009,
106314,
105082,
105133,
105227,
105228,
105815,
105196,
105227,
105238,
105244,
105274,
105276,
105286,
105303,
105308,
105332,
105346,
105347,
105381,
105630,
105667,
105674,
105679,
105711,
105686,
105767,
105789,
105830,
105813,
105815,
105849,
105852,
105855,
105863,
105890,
105913,
105933,
106011,
106056,
106058,
106117,
106064,
106156,
106164,
106172,
106187,
106193,
106201,
106206,
106292,
106308,
106314,
104578,
104631,
104753,
105942,
105198,
105323,
105942,
105983,
105942,
104446,
104569,
104592,
105867,
104841,
105243,
105317,
106319,
105595,
105693,
105867,
105879,
105905,
106070,
106191,
106195,
106224,
106242,
104894,
106219,
104510,
104539,
104545,
104553,
104560,
104555,
104488,
104588,
104598,
104605,
104606,
104610,
104613,
104611,
104612,
104599,
104638,
104637,
104639,
104648,
104649,
104652,
104656,
104659,
104679,
104687,
104690,
104703,
104686,
104714,
104713,
104720,
105799,
104712,
104735,
104743,
104747,
104750,
104752,
106288,
104761,
104765,
104768,
106286,
104779,
104783,
104785,
104795,
104789,
104779,
104797,
104792,
104799,
104800,
104819,
104815,
104816,
104824,
104828,
104829,
104827,
104831,
104807,
104832,
104834,
104837,
104853,
104857,
104864,
104858,
104862,
104866,
104867,
104869,
104871,
104874,
104875,
104890,
104891,
104892,
104896,
105983,
104899,
104912,
105303,
104918,
104922,
106191,
104950,
104969,
104978,
104979,
104989,
104988,
104994,
104997,
105000,
105004,
105005,
105008,
105014,
105018,
104686,
105036,
105040,
105044,
105046,
105049,
105068,
106222,
105055,
106168,
105059,
105070,
105071,
105073,
105075,
105074,
104687,
105091,
105090,
105092,
105093,
105098,
105102,
105114,
105115,
105117,
105120,
105123,
105129,
105140,
105143,
105316,
105359,
105156,
105159,
105162,
105161,
105717,
105165,
106174,
105179,
105180,
105182,
105193,
105208,
105265,
105230,
105212,
105209,
105216,
105223,
105224,
105225,
105236,
105259,
105245,
105246,
105249,
105258,
105256,
105636,
105299,
105284,
105327,
105294,
105301,
105304,
105315,
105321,
105316,
105313,
105311,
105333,
105356,
105351,
105352,
105354,
105358,
105359,
105700,
105367,
105376,
105601,
106318,
105602,
105603,
105621,
105682,
105644,
105641,
105642,
105639,
105645,
105717,
105653,
105657,
105658,
105661,
105707,
105662,
106015,
105668,
105708,
105671,
105683,
105696,
105697,
105692,
105718,
105719,
105729,
105816,
106261,
105743,
105742,
105873,
105762,
105765,
105769,
105770,
106294,
105779,
105780,
105782,
105788,
105792,
105793,
105796,
105798,
105799,
105800,
105808,
106127,
105809,
105835,
105839,
105848,
105847,
105860,
105861,
106143,
105866,
105872,
105881,
105883,
106126,
105892,
105906,
105917,
105919,
105922,
105923,
105926,
106127,
105935,
106140,
105943,
105949,
105984,
105993,
105995,
106010,
106016,
106098,
106055,
106060,
106174,
106167,
106168,
106173,
106177,
106178,
106182,
106186,
106196,
106277,
106288,
104572,
104939,
105053,
105080,
105218,
105357,
106142,
105801,
105918,
106141,
106293,
104748,
104835,
104986,
104926,
105325,
106171,
106077,
104707,
105912,
104983,
105300,
105618,
105912,
106101,
106042,
105772,
105775,
106137,
106137,
105898,
105978,
104382,
105118,
104717,
104804,
104805,
104897,
104925,
104995,
105038,
105118,
105131,
105139,
105142,
105146,
105945,
105335,
105670,
105672,
105727,
105965,
105856,
105969,
105945,
105982,
105955,
106161,
106026,
106127,
106230,
106300,
104529,
104414,
104873,
105103,
105747,
105998,
105771,
105375,
105366,
105998,
105744,
105747,
105771,
105777,
106078,
105998,
104900,
105809,
105725,
105282,
104540,
104579,
104706,
104671,
105282,
105330,
105695,
105232,
105204,
105619,
106188,
106218,
104725,
104725,
104762,
105219,
105810,
105996,
104705,
104773,
104787,
104793,
104971,
105793,
105253,
105651,
105888,
105900,
106282,
106311,
104952,
105030,
105121,
105278,
106002,
106113,
106113,
104651,
104523,
104535,
104537,
105065,
104552,
104594,
104603,
104607,
104624,
104689,
104708,
105736,
104731,
104740,
104643,
104976,
104651,
104825,
104666,
104670,
104669,
104678,
104673,
104682,
104684,
104694,
104698,
104699,
104696,
104704,
104709,
104730,
104813,
104830,
104733,
104729,
104861,
104966,
104962,
104902,
104906,
104909,
104916,
104921,
104933,
104963,
105048,
105095,
105109,
105113,
104698,
105141,
105035,
105065,
105066,
105069,
105078,
105116,
106048,
105157,
105862,
105191,
105200,
105203,
105242,
105260,
105255,
105261,
105288,
105292,
106224,
104501,
105338,
105337,
105373,
105593,
106165,
105350,
105716,
105652,
105355,
105361,
105365,
105368,
105378,
105592,
105605,
105631,
105649,
105709,
105864,
105685,
105688,
105734,
105736,
105740,
105824,
105754,
105755,
105756,
105864,
105773,
105778,
105846,
105838,
105970,
105862,
105891,
105894,
105960,
105915,
105920,
105924,
106315,
105928,
105932,
105944,
105946,
106001,
106044,
106047,
106048,
106097,
106174,
106150,
106158,
106165,
106179,
106296,
106306,
105640,
104766,
104803,
104859,
104955,
104959,
104936,
105042,
105214,
105821,
105380,
105596,
105656,
105726,
105761,
105821,
105931,
106125,
104550,
104875,
104619,
104734,
104758,
104772,
104770,
104784,
105213,
104887,
104930,
105027,
106320,
105088,
105148,
105328,
105213,
105229,
105291,
106160,
105264,
105307,
105328,
106320,
106312,
105626,
105643,
105690,
105678,
105687,
105784,
105966,
105957,
105973,
105976,
105987,
106159,
106160,
106169,
104635,
104801,
104823,
104958,
105105,
105318,
105217,
105617,
105636,
105640,
106250,
105702,
105916,
105901,
106071,
104951,
105171,
106138,
105823,
106138,
105902,
105281,
105265,
105615,
106120,
106192,
104888,
105616,
104565,
104778,
104893,
105817,
105604,
105087,
105752,
105271,
104615,
105081,
106180,
]
    for i in range(len(klist)):
        url="http://securities.stanford.edu/filings-case.html?id="+str(klist[i])
        result = urllib.request.urlopen(url)
        result = result.read()
        soup = bs(result,"lxml")
        si = soup.find("tr", {"class": "table-link"})
        attrs=si.attrs['onclick']
        downLink="http://securities.stanford.edu/"+attrs[17:len(attrs)-1]+','
        print(i)
        #str1 = ','.join(downLink)
        fd = open('downList.csv','a')
        fd.write(downLink)
        fd.close()
        #print(tr.attrs['onclik'])
    return downLink

def read_link():
    with open('list.csv', 'r') as f:
        reader = csv.reader(f)
        klist = list(reader)
    return klist


 
if __name__ == '__main__':
    main()