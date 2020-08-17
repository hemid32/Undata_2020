# -*- coding: UTF-8 -*-

import json
from bs4 import BeautifulSoup
import requests


class wiki():
    def __init__(self):
        self.url = "https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%AC%D8%B2%D8%A7%D8%A6%D8%B1"
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, "lxml")
        self.tbl = self.soup.find("table", {"class": "infobox infobox_v2 plainlist"})
        self.list_of_table_rows = self.tbl.findAll('tr')
        self.info_2 = {}
        self.info_3 = {}
        self.info = {}
        self.flag = []

    def delit_(self, x):
        m = ''
        for i in x:
            if i == '{' or i == '"' or i == '}' or i == ':' or i == "\W" or i == 'n':
                i = ''
            else:
                i = i
            m = m + i
        return m

    def get_flag(self, x):

        """ cett methode retune liste contient 3 valeur  val1 : url flag val2: url embadad val3: url map  """
        x = x.capitalize()
        url_flag = 'https://fr.wikipedia.org/wiki/Fichier:Flag_of_%s.svg' % (x)
        url_embadad = 'https://en.wikipedia.org/wiki/File:Emblem_of_%s.svg' % (x)
        url_map = 'https://en.wikipedia.org/wiki/File:%s_(orthographic_projection).svg' % (x)

        h = []

        for i in [url_flag, url_embadad, url_map]:
            if i == url_flag:
                y = 'Flag'
                tt = 'Fichier:%s of %s.svg' % (y, x)
                f = requests.get(i)
                soup = BeautifulSoup(f.text, "lxml")
                # tt = 'Fichier:%s of %s.svg'%(y , x)
                m = soup.find("img", {"alt": tt})
                src = str(m).split(' ')[9][8:]
                h.append(src)


            elif i == url_embadad:
                y = 'Emblem'
                tt = 'File:%s of %s.svg' % (y, x)
                f = requests.get(i)
                soup = BeautifulSoup(f.text, "lxml")
                # tt = 'Fichier:%s of %s.svg'%(y , x)
                m = soup.find("img", {"alt": tt})
                src = str(m).split(' ')[9][8:]
                h.append(src)


            else:
                tt = 'File:%s (orthographic projection).svg' % (x)
                f = requests.get(i)
                soup = BeautifulSoup(f.text, "lxml")
                # tt = 'Fichier:%s of %s.svg'%(y , x)
                m = soup.find("img", {"alt": tt})
                src = str(m).split(' ')[9][8:]
                h.append(src)

        return h

    def get_info(self, x):

        self.url = "https://ar.wikipedia.org/wiki/%s" % (x)
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, "lxml")
        self.tbl = self.soup.find("table", {"class": "infobox infobox_v2 plainlist"})
        self.list_of_table_rows = self.tbl.findAll('tr')
        self.info_2 = {}
        self.info_3 = {}
        self.info = {}
        self.flag = []
        self.url_flags = self.get_flag(x)
        self.kybord = [u'تاريخ التأسيس', u'عاصمة', u'تسمية السكان	', u'الكثافة السكانية', u'متوسط العمر',
                       u'نظام الحكم', u'رئيس الجمهورية', u'اللغة الرسمية', u'العملة'
            , u'← الإجمالي', u'للفرد', u'المؤشر', u'معدل البطالة']

        self.test = {}
        self.h = 1

        # for i  in self.kybord :

        for tr in self.list_of_table_rows:

            th = tr.find("th")
            td = tr.find("td")
            if th is not None and td is not None:
                    self.info[th.text] = td.text.strip()
                    # self.kybord = self.kybord[i+1:]
                    # print 'ouiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'
                    # break

                    """
                    if th is not None and i  in th.text :
                        if td is not None   :


                            self.info[i] = td.text.strip()
                            self.test[i] = self.h
                            self.h= self.h + 1

                            """
        print self.test

        for tr in self.list_of_table_rows:

            th = tr.find("th")
            td = tr.find("td")
            if th is None and td is not None:
                innerText_2 = ''
                # for elem_2 in td.previousGenerator():

                self.info_2[td.text] = td.text.strip()

        dec = json.dumps(self.info, indent=1, ensure_ascii=False).encode('utf8')
        dec_2 = json.dumps(self.info_2, indent=1, ensure_ascii=False).encode('utf8')
        # dec_3 = json.dumps(self.info_2, indent=1 , ensure_ascii=False).encode('utf8')
        information = self.delit_(dec)  # .split(',')
        logo_strng = self.delit_(dec_2).split(',')[3]
        # logo_imag  = self.flag
        return information


mm = wiki()
print  mm.get_info('algeria')