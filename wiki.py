#-*- coding: UTF-8 -*-

import json
from bs4 import BeautifulSoup
import requests


class wikip() :
    def __init__(self):
        self.url = "https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%AC%D8%B2%D8%A7%D8%A6%D8%B1"
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, "lxml")
        self.tbl = self.soup.find("table", {"class": "infobox infobox_v2"})
        self.list_of_table_rows = self.tbl.findAll('tr')
        self.info_2 = {}
        self.info_3 = {}
        self.info = {}
        self.flag = []


    def _delite_3(self,e) :

        for i in e:
            v1 = i.find('(')
            v2 = i.find(')')
            con1 = 0
            con2 = 0
            con3 = 0
            if v1 != -1 and v2 != -1:
                if v1 < v2:
                    h = e.index(i)
                    m = i[:v1] + i[v2 + 1:]
                    e[h] = m
                else:
                    h = e.index(i)
                    mm = i[:v2] + i[v2 + 1:]
                    e[h] = mm
            if v1 == -1 and v2 != -1:
                h = e.index(i)
                mmm = i[:v2:]
                e[h] = mmm
            if v2 == -1 and v1 != -1:
                h = e.index(i)
                mmmm = i[:v1:]
                e[h] = mmmm
        for i in e:
            v1 = i.find('[')
            v2 = i.find(']')
            if v1 != -1 and v2 != -1:
                if v1 < v2:
                    h = e.index(i)
                    ml = i[:v1] + i[v2 + 1:]
                    e[h] = ml
                else:
                    h = e.index(i)
                    mlm = i[:v2] + i[v2 + 1:]
                    e[h] = mlm
            if v1 == -1 and v2 != -1:
                h = e.index(i)
                mlml = i[:v2:]
                e[h] = mlml
            if v2 == -1 and v1 != -1:
                h = e.index(i)
                mlmlml = i[:v1:]
                e[h] = str(mlmlml).strip()
        coun1 = 0
        for i in e:
            v1 = i.find('(')
            v2 = i.find(')')
            v3 = i.find('[')
            v4 = i.find(']')

            if not (v1 == v2 and v1 == v3 and v1 == v4 and v1 == -1):
                coun1 = 1
        if coun1 == 1:
            return self._delite_3(e)

        return e




    def delit_2(self,e):
        for  i  in  e :
            m = ''
            for f in  i  :
                if f == "$"  or f == u'ملاحظة' :
                    f = ''
                    m = m+f
                else :
                    m = m+f
            e[e.index(i)] = m.strip()
        e_ = self._delite_3(e)
        return e_


    def delit_(self, x):
        m = ''
        for i in x:
            if i == '{' or i == '"' or i == '}' or i == ':' or i == "\W" or i == 'n':
                i = ''
            else:
                i = i
            m = m + i
        return  m

    def get_flag(self,x):


        pass

    def get_info(self,x):

        self.url = "https://ar.wikipedia.org/wiki/%s"%(x)
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, "lxml")
        self.tbl = self.soup.find("table", {"class": "infobox infobox_v2"})
        self.list_of_table_rows = self.tbl.findAll('tr')
        self.info_2 = {}
        self.info_3 = {}
        self.info = {}
        self.flag = []
        self.url_flags = self.get_flag(x)
        self.kybord = [u'تاريخ التأسيس',u'عاصمة',u'تسمية السكان',u'الكثافة السكانية',u'متوسط العمر',u'نظام الحكم',u'رئيس الجمهورية',u'اللغة الرسمية' ,u'العملة'
                        ,u'← الإجمالي',u'للفرد',u'المؤشر',u'معدل البطالة',u'جهة السير',u'نسبة المياه',u'السن القانونية',u'الرئيس',u'الملك']


        self.test = {}
        self.h = 1

        #for i  in self.kybord :
        i = 0
        flg = '*'
        while i < len(self.kybord) :
            for tr in self.list_of_table_rows:


                th = tr.find("th")
                td = tr.find("td")
                if th is not None and td is not None:
                    if self.kybord[i] in th.text :
                        self.info[self.kybord[i]] = td.text.strip()
                        #self.kybord = self.kybord[i+1:]
                        #print 'ouiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
                        #break
                        i = i + 1
                        break
                if tr == self.list_of_table_rows[-1] :
                    self.info[self.kybord[i]] = flg #u'غ.م'
                    flg = flg + '*'
                    i = i + 1




        for tr in self.list_of_table_rows:


            th = tr.find("th")
            td = tr.find("td")
            kk = [u'']
            if  th is  None and td is not None :
                innerText_2=''
                #for elem_2 in td.previousGenerator():



                self.info_2[td.text] =  td.text









        dec = json.dumps(self.info, indent=1 , ensure_ascii=False).encode('utf8')
        dec_2 = json.dumps(self.info_2, indent=1 , ensure_ascii=False).encode('utf8')
        #dec_3 = json.dumps(self.info_2, indent=1 , ensure_ascii=False).encode('utf8'
        #print dec# )
        information  = self.delit_(dec)#.split(',')
        logo_strng  = self.delit_(dec_2).split(',')[3]
        #logo_imag  = self.flag
        h = []
        p = []
        #print dec
        for i in  self.info.values() :
            h.append(i)
        for mm in  self.info_2.values() :
            p.append(mm)


        valeu = []
        valeu2 = []
        for i in self.delit_2(h) :
            valeu.append(i)
            #print i
        for ii in self.delit_2(p) :
            valeu2.append(ii)


        ky = u'الشعار الوطني'

        h = ''

        if ky in valeu2[3] :
            h = valeu2[3].replace(ky , '')
            valeu2[3] = h




        return  [valeu,valeu2]



