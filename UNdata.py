#-*- coding: UTF-8 -*-

import json
from bs4 import BeautifulSoup
import requests
import requests
import lxml.html as lh
import pandas as pd
from urllib import urlopen

url = "https://data.un.org/en/iso/dz.html"
r = requests.get(url)
"""soup = BeautifulSoup(self.r.text, "lxml")
tbl = self.soup.find("table", {"class": "infobox infobox_v2"})
list_of_table_rows = self.tbl.findAll('tr')
l = r.content
print(l)"""

lst = [0]*20
def deco(x):
    z=[]
    w = []
    for i in x:
        w.append(i)
        if len(w) == 4:
            z.append(w)
            w = []
    return z

def reu_data(x):

    #shipUrl = 'https://data.un.org/en/iso/dz.html'
    shipUrl = url_return(x)

    shipPage = urlopen(shipUrl)

    soup = BeautifulSoup(shipPage, 'xml')
    table = soup.find_all("table", {"class": "pure-table"})
    for mytable in table:
        table_body = mytable.find('tbody')

        rows = table_body.find_all('tr')
        for tr in rows:
            cols = tr.find_all('td')
            h = []
            for td in cols:
                # print td.text
                h.append(td.text)
            # print len(h)
            # print h


            if len(h) > 3:

                # print'yes'
                # pass
                # l = deco(h)
                # l = deco(h)
                # print(l)
                # for i in h :
                #    print i
                # print h
                for i in deco(h):
                    #print i
                    ajeut_valfromlst(i)
                    #print i
                    pass
                    if 'UN membership date' == i[0]:
                        # print ('UN membership date hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh : '  ,i )
                        pass
            else:
                # print 'nooo'
                # pass
                #print 'hhhhhhhhhhhhh : ', h
                ajeut_valfromlst(h)
    return  lst



def deco(x):
    z=[]
    w = []
    for i in x:
        w.append(i)
        if len(w) == 4:
            z.append(w)
            w = []
    return z



#print deco([10]*12)
"""shipUrl = 'https://data.un.org/en/iso/dz.html'
shipPage = urlopen(shipUrl)

soup = BeautifulSoup(shipPage , 'xml')
table = soup.find_all("table", { "class" : "pure-table" })
for mytable in table:
    table_body = mytable.find('tbody')
    try:
        rows = table_body.find_all('tr')
        for tr in rows:
            cols = tr.find_all('td')
            h = []
            for td in cols:
                #print td.text
                h.append(td.text)
            if len(h) > 3 :
                print'yes'
                #pass
                #print(deco(list(h)))
    except:
        print "no tbody"
"""

def delet_vide(x):
    # delet vide and caracter
    l = ''
    for i in x :
        if i == ' '  or  i not in ['1','2','3','4','5','6','7','8','9','0' , '.',] :
            pass
        else:
            l = l+i
    return  l



def ajeut_valfromlst(lis_val):
    if ( 'Capital city pop.(000, 2019)' in lis_val ):
        # عذذ سكان العاصمة
        #print 'yessss'
        ll = delet_vide(lis_val[2])
        pop  = int(float(ll)*1000)
        lst[0] = str(pop)

    if ('UN membership date' in lis_val):
        #  تاريخ الانظمام للامم المتحدة
        lst[1] = lis_val[2]
    if ('Sex ratio(m per 100 f)' in lis_val):
        # نسبة الجنس الذكور
        x = float(delet_vide(lis_val[2])) * 50/100
        lst[2] = str(x)
        #print  lst
    if ('Exchange rate(per US$)' in lis_val):
        # قيمة العملة مقابل الدولار
        #print  lis_val
        lst[3] = delet_vide(lis_val[2])


    if ( 'Economy: Agricultur' in lis_val[0]  or 'Economy: Agriculturec,d(% of Gross Value Added)' in lis_val ):
        # نسبة الاقتصاد الزراعي
        #print 'ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg' , lis_val
        lst[4] = delet_vide(lis_val[3])
    if ( 'Economy: Indust' in lis_val[0] or 'Economy: Industryc,d(% of Gross Value Added)' in lis_val):
        # نسبة الاقتصاد الصناعي
        lst[5] = lis_val[3][:-1]
    if ( 'Economy: Servi' in lis_val[0] or 'Economy: Services and other activityc,d(% of GVA)' in lis_val):
        # نسبة الاقتصاد الخدمات و الانشطة الاخرى
        lst[6] = lis_val[3][:-1]
    if ( 'Employment: Agricult' in lis_val[0] or'Employment: Agriculturee(% of employed)' in lis_val):
        # نسبة العمل في المجال الزراعي
        lst[7] = lis_val[3]
    if ( 'Employment: Indust' in lis_val[0] or 'Employment: Industrye(% of employed)' in lis_val):
        # نسبة العمل في المجال ا لصناعي
        lst[8] = lis_val[3]
    if ( 'Employment: Servi' in lis_val[0] or 'Employment: Servicese(% employed)' in lis_val ):
        # العمل في مجال الخدمات
        lst[9] = lis_val[3]
    if ( 'International trade: Expor' in lis_val[0] or 'International trade: Exportsj(million current US$)' in lis_val ):
        #  التجارة الدولية الصادرات مليون دولار
        ll = int(delet_vide(lis_val[3][:-3]))*1000000
        lst[10] = str(ll)
    if ( 'International trade: Imp' in lis_val[0] or  'International trade: Importsj(million current US$)' in lis_val ):
        # التجارة الدولية الواردات
        ll = int(delet_vide(lis_val[3][:-3])) * 1000000
        lst[11] = str(ll)
    if ('International trade: Ba' in lis_val[0]  or  'International trade: Balancej(million current US$)' in lis_val):
        # التجارة الدولية التوازن
        ll = int(delet_vide(lis_val[3][:-3])) * 1000000
        lst[12] = str(ll)
    if ('International migrant sto' in lis_val[0] or  'International migrant stock(000/% of total pop.)' in lis_val):
        #  عدد المهاجريين الدوليين نسبة مؤوية
        s = lis_val[3].find('/')
        prs =  delet_vide(lis_val[3][s + 1 :])

        #print(prs)
        lst[13] = prs
    if ('Health: Physi' in lis_val[0]):
        # نسبة الاطباء لكل 100 فرد
        try:
            lst[14] = str(float(delet_vide(lis_val[3])) / 10 )
        except :
            lst[14] = '...'
    if ('Education: Govern' in lis_val[0]):

        # نسبة الانفاق الحكومي من الناتج الاجمالي على التعليم
        lst[15] = delet_vide(lis_val[3])
    if ('Intentional homici' in lis_val[0]):
        # معدل جرائم القتل العمد لكل 100 فرد
        try:
            lst[16] = str(float(delet_vide(lis_val[3]))/1000)
        except :
            lst[16] = '...'
    if ('Seats held by women' in lis_val[0]):
        #  نسبة المقاعد التي تشغلها النساء في البرلمان
        lst[17] = delet_vide(lis_val[3])
    if ('Research  Development expenditure(% of GDP)' in lis_val):
        # نسبة الانفاق على البحث و التطوير
        lst[18] = delet_vide(lis_val[3])
    '''
    if ('Forested area(% of land area)' in lis_val):
        # نسبة الغابات من الارض
        lst[19] = delet_vide(lis_val[3])
    '''

    if ('Individuals using the Internet(per 100 inhabitants)' in lis_val):
        # نسبة الاشخاص الذين يستخدمن الانترنت
        lst[19] = delet_vide(lis_val[3])




    #print  lst
    '''
    if ('Exchange rate(per US$)' in lis_val):
        print  lis_val

        lst[2] = str(lis_val[2])[:-1]
        print  lst
        '''

def url_return(x) :
    dect = {'united-states-of-america': 'us', 'russia': 'ru', 'china': 'cn', 'india': 'in',
            'japan': 'jp', 'south-korea': 'kp', 'france': 'fr', 'united-kingdom': 'gb',
            'egypt': 'eg', 'brazil': 'br', 'turkey': 'tr',
            'italy': 'it', 'germany': 'de', 'iran': 'ir', 'pakistan':'pk',
            'indonesia': 'id', 'saudi-arabia': 'sa', 'israel': 'il',
            'australia': 'au', 'spain': 'es', 'poland': 'pl', 'vietnam': 'vn',
            'canada':'ca', 'north-korea': 'hk', 'taiwan': u'تايوان', 'ukraine': 'ua',
            'algeria': 'dz', 'south-africa': 'za', 'switzerland': 'ch', 'norway': 'no',
            'sweden': 'se', 'greece': 'gr', 'czech-republic':'cz',
            'myanmar': 'mm', 'netherlands': 'nl', 'colombia': 'co', 'mexico':'mx',
            'romania': 'ro', 'peru': 'pe', 'venezuela': 've', 'nigeria': 'ng',
            'argentina': 'ar', 'malaysia': 'my', 'united-arab-emirates': 'ae',
            'bangladesh': 'bd',
            'chile': 'cl', 'denmark': 'dk', 'iraq':'iq', 'singapore': 'sg',
            'syria': 'sy', 'morocco': 'ma', 'portugal': 'pt',
            'ethiopia':'et', 'serbia': 'rs', 'croatia': 'hr', 'belgium': 'be',
            'jordan': 'jo', 'cuba': 'cu', 'yemen':'ye',
            'oman': 'om', 'sudan': 'sd', 'libya':'ly', 'tunisia': 'tn', 'kuwait': 'kw',
            'qatar': 'qa',
            'bahrain': 'bh', 'ghana':'gh', 'south-sudan': 'ss', 'lebanon': 'lb',
            'thailand': 'th'}
    url = 'https://data.un.org/en/iso/'+ dect[x]  +'.html'
    return url

#print reu_data('japan')

