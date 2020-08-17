#-*- coding: UTF-8 -*-



import sys
from PyQt4 import QtCore, QtGui, uic , Qt
from PyQt4.QtGui import QApplication, QCompleter, QLineEdit, QStringListModel
#import mysql.connector
import time
import requests
import sqlite3
qtCreatorFile = "untitled.ui"  # Enter file here.
from index import creat_video
from wiki import wikip as wk
import traceback
from pickle import dump, load
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import  calcul_status
from  UNdata import  reu_data
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.bottun()
        self.databes()
        self.unite()
        self.auto_()
        #self.Auto_complete(0)
        self.line()
        self.target_vargul = False

    # هذي  الدالة تخدم مع يكيبيديا تعدل الاسم
    def wikii_cinfig_nome(self,x):

        m=''

        for i  in str(x) :
           if i == '-' :
                i = '_'
                m = m + i
           else :
               m =m+i
        return  m




    def sahp(self):
        self.UNdata()
        # هذي  الدالة تسحب المعلومات من الموقع و تعرضها في مكانها
        U = ['Defense Budget:', 'Mine Warfare:', 'Submarines:', 'Corvettes:', 'Destroyers:', 'Frigates:',
             'Aircraft Carriers:', 'Total Assets:', 'Attack Helicopters:', 'Helicopters:',
             'Trainers:', 'Transports:', 'Dedicated Attack:', 'Fighters:', 'Total Strength:', 'Rocket Projectors:',
             'Towed Artillery:', 'Self-Propelled Artillery:', 'Armored Vehicles:', 'Tanks:',
             'Reserve Personnel', 'Active Personnel', 'Total Military Personnel', 'Reaching Military Age Annually',
             'Fit-for-Service', 'Available Manpower', 'Total Population:', 'External Debt:', 'Proven Oil Reserves:',
             'Oil Consumption:', 'Oil Production:',
             'Usable Waterways:', 'Serviceable Airports:', 'Coastline Coverage:', 'Railway Coverage:',
             'Roadway Coverage:',
             'Square Land Area:']
        V = 'is ranked'
        try:

            Q = self.lineEdit_2.text()
            #print Q

            if 1 == 1:
                page = requests.get(Q)
                for row in U:
                    contents = page.content
                    m = str(contents).find(row)
                    m = str(contents)[m: m + 150]
                    f = m.find('span')
                    if 'ranked' in m and row != 'COMBAT TANKS:' and 'textOrange' not in m and 'textAquaBlue' not in m:
                        k = m[f: f + 20]  # 50 ===  20
                    else:
                        k = m[f: f + 100]
                    # k = m[f: f + 50]
                    # print(k)
                    i = 0
                    s = ''
                    while i < len(k):
                        if k[i] in '0123456789':
                            s = s + k[i]
                        else:
                            s = s + ''
                        i += 1

                    if s == "":
                        # s=''
                        contents = page.content
                        m = str(contents).find(row)
                        # m = str(contents)[m: m + 100]
                        k = str(contents)[m: m + 150]
                        while i < len(k):
                            if k[i] in '0123456789':
                                s = s + k[i]
                            else:
                                s = s + ''
                            i += 1

                    if U.index(row) == 0:
                        self.line1.setText(str(s))
                    if U.index(row) == 1 :
                        self.line3.setText(str(s))
                    if  U.index(row) == 2 :
                        self.line4.setText(str(s))
                    if U.index(row) == 3 :
                        self.line5.setText(str(s))
                    if U.index(row) == 4 :
                        self.line6.setText(str(s))
                    if U.index(row) == 5 :
                        self.line7.setText(str(s))
                    if U.index(row) == 6 :
                        self.line8.setText(str(s))
                    if U.index(row) == 7 :
                        self.line9.setText(str(s))
                    if U.index(row) == 8 :
                        self.line10.setText(str(s))
                    if U.index(row) == 9 :
                        self.line11.setText(str(s))
                    if U.index(row) == 10 :
                        self.line12.setText(str(s))
                    if U.index(row) == 11 :
                        self.line13.setText(str(s))
                    if U.index(row) == 12 :
                        self.line14.setText(str(s))
                    if U.index(row) == 13 :
                        self.line15.setText(str(s))
                    if U.index(row) == 14 :
                        self.line16.setText(str(s))
                    if U.index(row) == 15 :
                        self.line17.setText(str(s))
                    if U.index(row) == 16 :
                        self.line18.setText(str(s))
                    if U.index(row) == 17 :
                        self.line19.setText(str(s))
                    if U.index(row) == 18 :
                        self.line20.setText(str(s))
                    if U.index(row) == 19 :
                        self.line21.setText(str(s))
                    if U.index(row) == 20 :
                        self.line22.setText(str(s))
                    if U.index(row) == 21 :
                        self.line23.setText(str(s))
                    if U.index(row) == 22 :
                        self.line24.setText(str(s))
                    if U.index(row) == 23 :
                        self.line25.setText(str(s))
                    if U.index(row) == 24 :
                        self.line26.setText(str(s))
                    if U.index(row) == 25 :
                        self.line27.setText(str(s))
                    if U.index(row) == 26 :
                        self.line29.setText(str(s))
                        #pass

                    ############################################################################"

                    if U.index(row) == 27 :
                        self.line32.setText(str(s))
                    if U.index(row) == 28 :
                        self.line33.setText(str(s))
                    if U.index(row) == 29:
                        self.line34.setText(str(s))
                    if U.index(row) == 30:
                        self.line35.setText(str(s))
                    if U.index(row) == 31:
                        self.line36.setText(str(s))
                    if U.index(row) == 32:
                        self.line37.setText(str(s))
                    if U.index(row) == 33:
                        self.line38.setText(str(s))
                    if U.index(row) == 34:
                        self.line39.setText(str(s))
                    if U.index(row) == 35:
                        self.line40.setText(str(s))
                    if U.index(row) == 36:
                        self.line41.setText(str(s))

                    #######################################################################






            # هنا عرض تصنيف الدولة
            contents = page.content
            L = str(contents).find(V)
            N = str(contents)[L: L + 100]
            ss = N.find('textBold')
            NN = N[ss:ss + 13]

            print(NN)
            K = ''
            i = 0
            while i < len(NN):
                if NN[i] in '0123456789':
                    K = K + NN[i]
                else:
                    K = K + ''
                i += 1
            self.line31.setText(str(K))

            # الحصول على اسم الدولة
            S = str(Q).find('=')
            W = str(Q)[S+1:]
            self.line30.setText(W)

            #  هنا حتساب  النووي
            if W == 'united-states-of-america' :
                self.line2.setText('7200')
            elif W == 'russia' :
                self.line2.setText('7500')
            elif W == 'china' :
                self.line2.setText('260')
            elif W == 'india' :
                self.line2.setText('100')
            elif W == 'france' :
                self.line2.setText('300')
            elif W == 'united-kingdom':
                self.line2.setText('215')
            elif W == 'israel':
                self.line2.setText('120')
            elif W == 'pakistan':
                self.line2.setText('100')
            elif W == 'north-korea':
                self.line2.setText('12')
            else :
                self.line2.setText('0')

            Qt.QMessageBox.information(self, u'صحيت', u'تم سحب المعلومات  بنجاح ')


        except :

            #except Exception, e: print str(e)


            Qt.QMessageBox.critical(self, u'خطأ', u'خطأ في الانترنت او الرابط او هناك شيئ لا يعمل')



    # سحب المعلومات من موقع UNdata

    def UNdata(self):
        #from .UNdata


        Q = self.lineEdit_2.text()
        S = str(Q).find('=')
        w = str(Q)[S + 1:]
        UNdata1 = reu_data(w)
        UNdata = []
        for i in UNdata1 :
            UNdata.append(str(i))

        self.L7_0.setText(UNdata[1-1])
        self.L7_1.setText(UNdata[2-1])
        self.L7_2.setText(UNdata[3-1])
        self.L7_3.setText(UNdata[4-1])
        self.L7_4.setText(UNdata[5-1])
        self.L7_5.setText(UNdata[6-1])
        self.L7_6.setText(UNdata[7-1])
        self.L7_7.setText(UNdata[8-1])
        self.L7_8.setText(UNdata[9-1])
        self.L7_9.setText(UNdata[10-1])
        self.L8_0.setText(UNdata[11-1])
        self.L8_1.setText(UNdata[12-1])
        self.L8_2.setText(UNdata[13-1])
        self.L8_3.setText(UNdata[14-1])
        self.L8_4.setText(UNdata[15-1])
        self.L8_5.setText(UNdata[16-1])
        self.L8_6.setText(UNdata[17-1])
        self.L8_7.setText(UNdata[18-1])
        self.L8_8.setText(UNdata[19-1])
        self.L8_9.setText(UNdata[20-1])






    # عرض معلومات يكيبيديا


    def wiki_afich(self):

        Q = self.lineEdit_2.text()
        S = str(Q).find('=')
        W = str(Q)[S + 1:]

        nome = self.wikii_cinfig_nome(W)
        g  = wk()
        tab = g.get_info(str(nome))[0]    # سحب  المعلومات  الاساسية بدون الشعار و الرابط
        tab2 = g.get_info(str(nome))[1]  # معلمات الشعار   و و و الخ


        #print '**************************************************************
        flg_ = u'م.غ'

        for i  in tab :
            
            #print tab.index(i)

            if tab.index(i) == 0 :
                if '*' in i :
                    self.L1_7.setText(flg_)
                else :
                    #m = self.conv(i)
                    self.L1_7.setText(i)

            if tab.index(i) == 1 :
                if '*' in i :
                    self.L2_7.setText(u'م.غ')
                else :
                    m = self.conv(i)
                    self.L2_7.setText(m)
            if tab.index(i) == 2 :
                if '*' in  i :
                    self.L2_9.setText(flg_)
                else :
                    m = self.conv(i)
                    self.L2_9.setText(m)
            if tab.index(i) == 3 :
                if '*' in  i  :
                    self.L2_1.setText(flg_)
                else :
                    #m = self.conv(i)
                    self.L2_1.setText(i)
            if tab.index(i) == 4 :
                if '*' in  i  :
                    self.L1_10.setText(flg_)
                else :
                    m = self.conv(i)
                    self.L1_10.setText(m)
            if tab.index(i) == 5 :
                if '*' in  i  :
                    #self.L2_5.setText(flg_)
                    pass
                else  :
                    #m = self.conv(i)
                    self.L2_2.setText(i)
            if tab.index(i) == 6 :
                if  '*' in  i :
                    #self.L2_4.setText(flg_)
                    pass
                else :
                    #m = self.conv(i)
                    self.L2_2.setText(i)
            if self.L2_2.text() == '' :
                self.L2_2.setText(flg_)
            if tab.index(i) == 7 :
                #m = self.conv(i)
                if '*' in i :
                    self.L2_3.setText(flg_)
                else :
                    self.L2_3.setText(i)
            if tab.index(i) == 8 :
                #m = self.conv(i)
                if '*' in i:
                    self.L1_5.setText(flg_)
                else :
                    self.L1_5.setText(i)
            if tab.index(i) == 9 :
                if '*' in i :
                    self.L2_4.setText(flg_)
                else :
                    self.L2_4.setText(i)


            #################### L1_. #############################
            if tab.index(i) == 10 :
                #m = self.conv(i)
                if '*' in i:
                    self.L1_4.setText(flg_)
                else :
                    self.L1_4.setText(i)
            if tab.index(i) == 11 :
                #m = self.conv(i)
                if '*' in i:
                    self.L2_5.setText(flg_)
                else :
                    self.L2_5.setText(i)
            if tab.index(i) == 12 : ##########################
                m = self.conv(i)
                if '*' in i:
                    self.L1_8.setText(flg_)
                else :
                    self.L1_8.setText(m)
            if tab.index(i) == 13 :
                #m = self.conv(i)
                if '*' in i:
                    #self.L1_7.setText(flg_)
                    pass
                else :
                    self.L2_2.setText(i)
            if tab.index(i) == 14 :
                #m = self.conv(i)
                if '*' in i:
                    self.L6_9.setText(flg_)
                else :
                    self.L6_9.setText(i)
            if tab.index(i) == 15 :
                m = self.conv(i)
                if '*' in i:
                    self.L1_9.setText(flg_)
                else :
                    self.L1_9.setText(m)
            if tab.index(i) == 16 :
                m = self.conv(i)
                if '*' in i:
                    self.L2_10.setText(flg_)
                else :
                    self.L2_10.setText(m)
            if tab.index(i) == 17 :
                #m = self.conv(i)
                if '*' in i:
                    self.L2_6.setText(flg_)
                else :
                    self.L2_6.setText(i)
            self.L6_10.setText(u'غ.م')
            ############################################################
        # سجب الشعار
        if u'تعديل' in  tab2[3]  :
            self.L1_3.setText(u'غ.م')
        else :
            self.L1_3.setText(tab2[3])


        # دول العالم الال - الثاني  - الثالث

        pays1 = ['united-states-of-america' , 'canada','denmark','france','germany' , 'greece','united-kingdom','turkey',
                 'italy','spain','poland','czech-republic','netherlands','norway','romania','bulgaria','hungary',
                 'slovakia','portugal','belgium','croatia','lithuania','slovenia','albania','latvia','estonia',
                 'montenegro','japan','south-korea','israel','australia','austria','ireland','sweden','switzerland']
        pays2 = ['russia','china','cuba','lithuania','belarus','georgia','north-korea','vietnam']
        if W in pays1 :
            self.L2_8.setText(u'الاول')
        elif W in pays2 :
            self.L2_8.setText(u'الثاني')
        else :
            self.L2_8.setText(u'الثالث')






    # هذي الدالة ليكيبيديا تريقل الكلمات الي ارقام
    def  conv(self,x):
        h = ''
        for i in x :
            if i not in ['1','2','3','4','5','6','6','7','8','9','.','0',',']:
                i = ''
                h = h+i
            else :
                h = h+i
        return h



    def unite(self):
        self.setWindowTitle(u'ثقافة عسكرية')




    def databes(self):
        #self.dbe = mysql.connector.connect(host='localhost' , user='root', password='12345' ,db='mydb')
        #self.cur = self.dbe.cursor()

        ######
        file = ('data.db')
        self.conn = sqlite3.connect(file)
        self.cur =  self.conn.cursor()

        sql = ''' SELECT * FROM table_1 '''
        m = self.comboBox.currentText()
        f = [str(m)]

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for e in  data :
            l = e[28]
            self.comboBox.addItem(str(l))








    def bottun(self):
        self.pushButton.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(self.add_l)
        self.pushButton_4.clicked.connect(self.demare)
        self.pushButton_2.clicked.connect(self.tte)
        self.pushButton_5.clicked.connect(self.ubdite)
        self.pushButton_6.clicked.connect(self.delit)
        self.pushButton_7.clicked.connect(self.sahp)
        self.pushButton_8.clicked.connect(self.hhhh)
        self.pushButton_9.clicked.connect(self.vers_cod_creat_video)
        self.pushButton_9.clicked.connect(self.clacu_l_comparing)
        self.pushButton_10.clicked.connect(self.open_img_1)
        self.pushButton_11.clicked.connect(self.open_img_2)
        self.pushButton_13.clicked.connect(self.wiki_afich)
        self.pushButton_14.clicked.connect(self.open_img_map)
        self.pushButton_15.clicked.connect(self.open_img_embad)
        self.pushButton_16.clicked.connect(self.open_imag_as)
        self.pushButton_17.clicked.connect(self.calcul_staus_appal)







    def tte(self):
        self.line1.setText(str("{:,}".format(int(self.line1.text()))))
        self.line22.setText(str("{:,}".format(int(self.line22.text()))))
        self.line23.setText(str("{:,}".format(int(self.line23.text()))))
        self.line24.setText(str("{:,}".format(int(self.line24.text()))))
        self.line25.setText(str("{:,}".format(int(self.line25.text()))))
        self.line26.setText(str("{:,}".format(int(self.line26.text()))))
        self.line27.setText(str("{:,}".format(int(self.line27.text()))))
        self.line29.setText(str("{:,}".format(int(self.line29.text()))))
        self.line19.setText(str("{:,}".format(int(self.line19.text()))))
        self.line18.setText(str("{:,}".format(int(self.line18.text()))))
        self.line20.setText(str("{:,}".format(int(self.line20.text()))))
        self.line21.setText(str("{:,}".format(int(self.line21.text()))))
        self.line32.setText(str("{:,}".format(int(self.line32.text()))))
        self.line33.setText(str("{:,}".format(int(self.line33.text()))))
        self.line34.setText(str("{:,}".format(int(self.line34.text()))))
        self.line35.setText(str("{:,}".format(int(self.line35.text()))))
        self.line36.setText(str("{:,}".format(int(self.line36.text()))))
        self.line37.setText(str("{:,}".format(int(self.line37.text()))))
        self.line38.setText(str("{:,}".format(int(self.line38.text()))))
        self.line39.setText(str("{:,}".format(int(self.line39.text()))))
        self.line40.setText(str("{:,}".format(int(self.line40.text()))))
        self.line41.setText(str("{:,}".format(int(self.line41.text()))))
        #self.line42.setText(str("{:,}".format(int(self.line42.text()))))


        self.L8_0.setText(str("{:,}".format(int(self.L8_0.text()))))
        self.L7_0.setText(str("{:,}".format(int(self.L7_0.text()))))
        self.L8_1.setText(str("{:,}".format(int(self.L8_1.text()))))
        self.L8_2.setText(str("{:,}".format(int(self.L8_2.text()))))
        self.target_vargul = True




    def add(self):
        ########################################### wikibidia #################


        #########################################################################


        line1 = self.line1.text()
        line2 = self.line2.text()
        line3 = self.line3.text()
        line4 = self.line4.text()
        line5 = self.line5.text()
        line6 = self.line6.text()
        line7 = self.line7.text()
        line8 = self.line8.text()
        line9 = self.line9.text()
        line10 = self.line10.text()
        line11 = self.line11.text()
        line12 = self.line12.text()
        line13 = self.line13.text()
        line14 = self.line14.text()
        line15 = self.line15.text()
        line16 = self.line16.text()
        line17 = self.line17.text()
        line18 = self.line18.text()
        line19 = self.line19.text()
        line20 = self.line20.text()
        line21 = self.line21.text()
        line22 = self.line22.text()
        line23 = self.line23.text()
        line24 = self.line24.text()
        line25 = self.line25.text()
        line26 = self.line26.text()
        line27 = self.line27.text()
        line29 = self.line29.text()
        line30 = self.line30.text()
        line31 = self.line31.text()
        ############################################add 2019
        line32 = self.line32.text()
        line33 = self.line33.text()
        line34 = self.line34.text()
        line35 = self.line35.text()
        line36 = self.line36.text()
        line37 = self.line37.text()
        line38 = self.line38.text()
        line39 = self.line39.text()
        line40 = self.line40.text()
        line41 = self.line41.text()
        #############################################################"
        # UNdata
        L7_0 = self.L7_0.text()
        L7_1 = unicode(self.L7_1.text())
        L7_2 = self.L7_2.text()
        L7_3 = self.L7_3.text()
        L7_4 = self.L7_4.text()
        L7_5 = self.L7_5.text()
        L7_6 = self.L7_6.text()
        L7_7 = self.L7_7.text()
        L7_8 = self.L7_8.text()
        L7_9 = self.L7_9.text()
        L8_0 = self.L8_0.text()
        L8_1 = self.L8_1.text()
        L8_2 = self.L8_2.text()
        L8_3 = self.L8_3.text()
        L8_4 = self.L8_4.text()
        L8_5 = self.L8_5.text()
        L8_6 = self.L8_6.text()
        L8_7 = self.L8_7.text()
        L8_8 = self.L8_8.text()
        L8_9 = self.L8_9.text()



        ############################################################


        #self.cur.execute('''INSERT INTO table(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30))
        #self.cur.execute('''INSERT INTO
        #                          table_1(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30,line31)
        #                          VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30,line31))
        if line1 == '' or line2 == ''  or line3 == '' or line4 == '' or line5 == '' or\
                line6 == '' or line7 == '' or line8 == '' or line9 == '' or line10 == '' or  line11 == '' or\
                line12 == '' or line13 == '' or line14 == '' or line15 == '' or  line16 == '' or line17 == '' or line18 == '' or\
                line19 == '' or line20 == '' or line21 == '' or line22 == '' or line23 == ''  or line24 == '' or line25 == '' or line26 == '' or\
                line27 == ''  or line29 == '' or  line30 == '' or line31 == '' or line32 == ''  or line33 == '' or line34 == '' \
                or line35 == '' or line36 == '' or line37 == '' or line38 == '' or line39 == '' or line40 == '' or line41 == '' :






            Qt.QMessageBox.critical(self, u'خطأ', u'نسيت مكان فارغ')
        else  :

            #####################################add 2019 ##################"
            file = ('data.db')
            self.conn = sqlite3.connect(file)
            self.cur = self.conn.cursor()
            #############################################################"

            sql = ''' SELECT * FROM table_1 '''
            self.cur.execute(sql)
            data = self.cur.fetchall()
            i = 0
            m = 0

            while i < len(data) :
                if data[i][28]  == self.line30.text() :
                    m=m+1
                i+=1



            if m != 0 :
                Qt.QMessageBox.critical(self, u'خطأ', u'هذي  الدولة موجودة مسبقايمكنك تعديل معلوماتها')
                self.demare()

            else :
                self.cur.execute('''INSERT INTO 
                                                  table_1(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line29,line30,line31,line32,line33,line34,line35,line36,line37,line38,line39,line40,line41,
                                                  L7_0 , L7_1 , L7_2 , L7_3 , L7_4 , L7_5 ,L7_6  , L7_7 , L7_8 , L7_9 , L8_0 , L8_1 , L8_2 , L8_3 , L8_4 , L8_5 , L8_6 , L8_7 , L8_8 , L8_9)
                                                  VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s' )''' % (
                line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14,
                line15, line16, line17, line18, line19, line20, line21, line22, line23, line24, line25, line26, line27,
                line29, line30, line31 , line32,line33,line34,line35,line36,line37,line38,line39,line40,line41 , L7_0 , L7_1 , L7_2 , L7_3 , L7_4 , L7_5 ,L7_6  , L7_7 , L7_8 , L7_9 , L8_0 , L8_1 , L8_2 , L8_3 , L8_4 , L8_5 , L8_6 , L8_7 , L8_8 , L8_9))
                self.conn.commit()
                m = self.line30.text()
                self.comboBox.addItem(m)
                Qt.QMessageBox.information(self, u'صحيت', u'تم اضافة الدولة الي قاعدة البايانات بنجاح')






    def delit(self):
        #####################################add 2019 ##################"
        file = ('data.db')
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        #############################################################"

        line30 = self.line30.text()
        if line30 != '' :
            sql = ''' SELECT * FROM table_1 WHERE line30 = %s '''
            m = self.line30.text()
            f = str(m)

            self.cur.execute(''' SELECT * FROM table_1 WHERE line30 = '%s' '''%f)
            data = self.cur.fetchall()
            if data == []:
                Qt.QMessageBox.critical(self, u'حطأ', u' هذه الدولة غير موجودة في قاعة البيانات')
            else :

                self.cur.execute(''' DELETE FROM table_1  WHERE  line30 = '%s'  '''%(line30 ,))
                self.conn.commit()
                Qt.QMessageBox.information(self, u'صحيت', u'تم الحذف  بنجاح')




        else :
            Qt.QMessageBox.critical(self, u'خطأ', u'لم تضع اسم الدولة مراد حذفها')






    def ubdite(self):

        #####################################add 2019 ##################"
        file = ('data.db')
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        #############################################################"

        line1 = self.line1.text()
        line2 = self.line2.text()
        line3 = self.line3.text()
        line4 = self.line4.text()
        line5 = self.line5.text()
        line6 = self.line6.text()
        line7 = self.line7.text()
        line8 = self.line8.text()
        line9 = self.line9.text()
        line10 = self.line10.text()
        line11 = self.line11.text()
        line12 = self.line12.text()
        line13 = self.line13.text()
        line14 = self.line14.text()
        line15 = self.line15.text()
        line16 = self.line16.text()
        line17 = self.line17.text()
        line18 = self.line18.text()
        line19 = self.line19.text()
        line20 = self.line20.text()
        line21 = self.line21.text()
        line22 = self.line22.text()
        line23 = self.line23.text()
        line24 = self.line24.text()
        line25 = self.line25.text()
        line26 = self.line26.text()
        line27 = self.line27.text()
        line29 = self.line29.text()
        line30 = self.line30.text()
        line31 = self.line31.text()
        ###############################################add 2019 ##########################
        line32 = self.line32.text()
        line33 = self.line33.text()
        line34 = self.line34.text()
        line35 = self.line35.text()
        line36 = self.line36.text()
        line37 = self.line37.text()
        line38 = self.line38.text()
        line39 = self.line39.text()
        line40 = self.line40.text()
        line41 = self.line41.text()
        ##################################################################################
        ##### wikibidia #####
        image_map = self.L1_12.text()
        image_embdad = self.L1_6.text()
        embadad = self.L1_3.text()
        tasis = self.L1_4.text()
        asima = self.L1_5.text()
        image_asima = self.L1_11.text()
        tasmiat_sokan = self.L1_7.text()
        katafa = self.L1_8.text()
        motawasit_omr = self.L1_9.text()
        sen_9anoni = self.L1_10.text()
        nidam_hokm = self.L2_1.text()
        rais = self.L2_2.text()
        longage = self.L2_3.text()
        omla = self.L2_4.text()
        jihat_sir = self.L2_5.text()
        nateg_mahali_ij = self.L2_6.text()
        nateg_mahali_fr = self.L2_7.text()
        doal_alam = self.L2_8.text()
        moachir_tanmia = self.L2_9.text()
        moadal_batala = self.L2_10.text()
        nisbat_miah = self.L6_9.text()
        #nisbat_miah = self.L6_9.text()
        add_horob = self.L6_10.text()


        #######################################
        # UNdata
        L7_0 = self.L7_0.text()
        L7_1 = unicode(self.L7_1.text())
        L7_2 = self.L7_2.text()
        L7_3 = self.L7_3.text()
        L7_4 = self.L7_4.text()
        L7_5 = self.L7_5.text()
        L7_6 = self.L7_6.text()
        L7_7 = self.L7_7.text()
        L7_8 = self.L7_8.text()
        L7_9 = self.L7_9.text()
        L8_0 = self.L8_0.text()
        L8_1 = self.L8_1.text()
        L8_2 = self.L8_2.text()
        L8_3 = self.L8_3.text()
        L8_4 = self.L8_4.text()
        L8_5 = self.L8_5.text()
        L8_6 = self.L8_6.text()
        L8_7 = self.L8_7.text()
        L8_8 = self.L8_8.text()
        L8_9 = self.L8_9.text()





        ######################
        sql = ''' SELECT * FROM table_1 WHERE line30 = %s '''
        m = self.line30.text()
        f = str(m)

        self.cur.execute(''' SELECT * FROM table_1 WHERE line30 = '%s' '''%f)
        data = self.cur.fetchall()
        if  data == [] :
            Qt.QMessageBox.critical(self,u'خطأ',u'هذه الدولة غير موجودة في قاعدة البيانات')
        else :
            self.cur.execute(''' UPDATE  table_1
                                            SET
                                            line1 = '%s',line2 = '%s',line3 = '%s',line4 = '%s',line5 = '%s',line6 = '%s',line7 = '%s',line8 = '%s',line9 = '%s',line10 = '%s',line11 = '%s',line12 = '%s',line13 = '%s',line14 = '%s',line15 = '%s',line16 = '%s',line17 = '%s',line18 = '%s',line19 = '%s',line20 = '%s',line21 = '%s',line22 = '%s',line23 = '%s',line24 = '%s',line25 = '%s',line26 = '%s',line27 = '%s',line29 = '%s',line30 = '%s',line31 = '%s',line32 = '%s',line33 = '%s',line34 = '%s',line35 = '%s',line36 = '%s',line37 = '%s',line38 = '%s',line39 = '%s',line40 = '%s',line41 = '%s',
                                            image_map = '%s' , image_embdad = '%s' , embadad = '%s' , tasis = '%s' , asima = '%s' , image_asima = '%s' , tasmiat_sokan = '%s' , katafa_sokania = '%s' , motawasit_omr = '%s' , sen_9anoni = '%s' , nidam_hokm = '%s' , rais = '%s' , longage = '%s' , omla = '%s' ,jihat_sir = '%s' , nateg_mahali_ij = '%s' ,  nateg_mahali_fr = '%s' , doal_alam = '%s' , moachir_tanmia = '%s' , moadal_batala = '%s' , nisbat_miah  = '%s' ,  add_horob  = '%s'    , L7_0  = '%s'  , L7_1  = '%s' , L7_2  = '%s' , L7_3  = '%s'  , L7_4  = '%s'  , L7_5  = '%s'  ,L7_6   = '%s' , L7_7  = '%s' , L7_8  = '%s'  , L7_9  = '%s'  , L8_0  = '%s'  , L8_1  = '%s'  , L8_2  = '%s'  , L8_3  = '%s'  , L8_4 = '%s'  , L8_5  = '%s'  , L8_6   = '%s' , L8_7  = '%s' , L8_8  = '%s' , L8_9  = '%s'  
                                            WHERE
                                            line30 = '%s' ; '''%(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14,
                                                                 line15, line16, line17, line18, line19, line20, line21, line22, line23, line24, line25, line26, line27,
                                                                 line29,line30,line31,line32,line33,line34,line35,line36,line37,line38,line39,line40,line41,
                                                                 image_map , image_embdad , embadad ,tasis , asima ,image_asima ,tasmiat_sokan , katafa , motawasit_omr,
                                                                 sen_9anoni,nidam_hokm,rais,longage,omla,jihat_sir,nateg_mahali_ij,nateg_mahali_fr,doal_alam,moachir_tanmia,moadal_batala,
                                                                 nisbat_miah,add_horob , L7_0 , L7_1 , L7_2 , L7_3 , L7_4 , L7_5 ,L7_6  , L7_7 , L7_8 , L7_9 , L8_0 , L8_1 , L8_2 , L8_3 , L8_4 , L8_5 , L8_6 , L8_7 , L8_8 , L8_9   ,line30  ))
            #print 'ok'

            if line1 == '' or line2 == '' or line3 == '' or line4 == '' or line5 == '' or \
                    line6 == '' or line7 == '' or line8 == '' or line9 == '' or line10 == '' or line11 == '' or \
                    line12 == '' or line13 == '' or line14 == '' or line15 == '' or line16 == '' or line17 == '' or line18 == '' or \
                    line19 == '' or line20 == '' or line21 == '' or line22 == '' or line23 == '' or line24 == '' or line25 == '' or line26 == '' or \
                    line27 == '' or line29 == '' or line30 == '' or line31 == '' or line32 == '' or line33 == '' or line34 == '':

                Qt.QMessageBox.critical(self, u'خطأ', u'نسيت احد المعلومات تركته فارغ -_-')
            else:

                #self.conn.commit()
                self.conn.commit()
                m = self.line30.text()
                self.comboBox.addItem(m)
                Qt.QMessageBox.information(self, u'صحيت', u'تم التعديل بنجاح شكرا سي بن عامر')



        ########################








    def add_l(self):
        #####################################add 2019 ##################"
        file = ('data.db')
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        #############################################################"

        line1 = self.line1.text()
        line2 = self.line2.text()
        line3 = self.line3.text()
        line4 = self.line4.text()
        line5 = self.line5.text()
        line6 = self.line6.text()
        line7 = self.line7.text()
        line8 = self.line8.text()
        line9 = self.line9.text()
        line10 = self.line10.text()
        line11 = self.line11.text()
        line12 = self.line12.text()
        line13 = self.line13.text()
        line14 = self.line14.text()
        line15 = self.line15.text()
        line16 = self.line16.text()
        line17 = self.line17.text()
        line18 = self.line18.text()
        line19 = self.line19.text()
        line20 = self.line20.text()
        line21 = self.line21.text()
        line22 = self.line22.text()
        line23 = self.line23.text()
        line24 = self.line24.text()
        line25 = self.line25.text()
        line26 = self.line26.text()
        line27 = self.line27.text()
        line29 = self.line29.text()
        line30 = self.line30.text()
        line31 = self.line31.text()

        #sql = ''' SELECT * FROM table_1 WHERE line30 = %s '''
        m = self.line30.text()
        f = str(m)

        self.cur.execute(''' SELECT * FROM table_1 WHERE line30 =  '%s' '''%f)
        data = self.cur.fetchall()
        if data == []:
            Qt.QMessageBox.critical(self, u'حطأ', u' هذه الدولة غير موجودة في قاعة البيانات')

        else  :



            #sql = ''' SELECT * FROM table_1 WHERE line30 = %s '''
            m = self.comboBox.currentText()
            f = str(m)

            self.cur.execute(''' SELECT * FROM table_1 WHERE line30 =  '%s' '''%f)
            data = self.cur.fetchall()
            for row in data:
                p =  list(row)




            l = self.lineEdit.text()
            self.lineEdit.setText(l + '+' + str(p[28]))

            self.line1.setText( str(int(p[0]) + int(self.line1.text()) ))
            self.line2.setText( str(int(p[1]) + int(self.line2.text()) ))
            self.line3.setText( str(int(p[2]) + int(self.line3.text()) ))
            self.line4.setText( str(int(p[3]) + int(self.line4.text()) ))
            self.line5.setText( str(int(p[4]) + int(self.line5.text()) ))
            self.line6.setText( str(int(p[5]) + int(self.line6.text()) ))
            self.line7.setText( str(int(p[6]) + int(self.line7.text()) ))
            self.line8.setText( str(int(p[7]) + int(self.line8.text()) ))
            self.line9.setText( str(int(p[8]) + int(self.line9.text()) ))
            self.line10.setText( str(int(p[9]) + int(self.line10.text()) ))
            self.line11.setText( str(int(p[10]) + int(self.line11.text()) ))
            self.line12.setText( str(int(p[11]) + int(self.line12.text()) ))
            self.line13.setText( str(int(p[12]) + int(self.line13.text()) ))
            self.line14.setText( str(int(p[13]) + int(self.line14.text()) ))
            self.line15.setText( str(int(p[14]) + int(self.line15.text()) ))
            self.line16.setText( str(int(p[15]) + int(self.line16.text()) ))
            self.line17.setText( str(int(p[16]) + int(self.line17.text()) ))
            self.line18.setText( str(int(p[17]) + int(self.line18.text()) ))
            self.line19.setText( str(int(p[18]) + int(self.line19.text()) ))
            self.line20.setText( str(int(p[19]) + int(self.line20.text()) ))
            self.line21.setText( str(int(p[20]) + int(self.line21.text()) ))
            self.line22.setText( str(int(p[21]) + int(self.line22.text()) ))
            self.line23.setText( str(int(p[22]) + int(self.line23.text()) ))
            self.line24.setText( str(int(p[23]) + int(self.line24.text()) ))
            self.line25.setText( str(int(p[24]) + int(self.line25.text()) ))
            self.line26.setText( str(int(p[25]) + int(self.line26.text()) ))
            self.line27.setText( str(int(p[26]) + int(self.line27.text()) ))
            self.line29.setText( str(int(p[27]) + int(self.line29.text()) ))
            self.line30.setText(str(p[28]))
            self.line31.setText(str(p[29]))
            self.line32.setText(str(int(p[30]) + int(self.line32.text())))
            self.line33.setText(str(int(p[31]) + int(self.line33.text())))
            self.line34.setText(str(int(p[32]) + int(self.line34.text())))
            self.line35.setText(str(int(p[33]) + int(self.line35.text())))
            self.line36.setText(str(int(p[34]) + int(self.line36.text())))
            self.line37.setText(str(int(p[35]) + int(self.line37.text())))
            self.line38.setText(str(int(p[36]) + int(self.line38.text())))
            self.line39.setText(str(int(p[37]) + int(self.line39.text())))
            self.line40.setText(str(int(p[38]) + int(self.line40.text())))
            self.line41.setText(str(int(p[39]) + int(self.line41.text())))

            ### UNdata add
            try:
                self.L7_0.setText(str(int(p[61 + 1]) + int(self.L7_0.text())))
            except :
                self.L7_0.setText(str(p[61 + 1]))
            try:
                self.L7_1.setText(p[62+1])
            except:
                pass
            try:
                self.L7_2.setText(str(float(p[63 + 1]) + float(self.L7_2.text())))
            except:
                self.L7_2.setText(str(p[63 + 1]))

            try:
                self.L7_3.setText(str(float(p[64 + 1]) + float(self.L7_3.text())))
            except:
                self.L7_3.setText(str(p[64 + 1]))

            try:
                self.L7_4.setText(str(float(p[65 + 1]) + float(self.L7_4.text())))
            except:
                self.L7_4.setText(str(p[65 + 1]))

            try:
                self.L7_5.setText(str(float(p[66 + 1]) + float(self.L7_5.text())))
            except :
                self.L7_5.setText(str(p[66 + 1]))

            try:
                self.L7_6.setText(str(float(p[67 + 1]) + float(self.L7_6.text())))
            except:
                self.L7_6.setText(str(p[67 + 1]))

            try:
                self.L7_7.setText(str(float(p[68 + 1]) + float(self.L7_7.text())))
            except:
                self.L7_7.setText(str(p[68 + 1]))

            try:
                self.L7_8.setText(str(float(p[69 + 1]) + float(self.L7_8.text())))
            except:
                self.L7_8.setText(str(p[69 + 1]))

            try:
                self.L7_9.setText(str(float(p[70 + 1]) + float(self.L7_9.text())))
            except :
                self.L7_9.setText(str(p[70 + 1]))
            try:
                self.L8_0.setText(str(int(p[71 + 1]) + int(self.L8_0.text())))
            except:
                self.L8_0.setText(str(p[71 + 1]))

            try:
                self.L8_1.setText(str(int(p[72 + 1]) + int(self.L8_1.text())))
            except:
                self.L8_1.setText(str(p[72 + 1]))
            try:
                self.L8_2.setText(str(int(p[73 + 1]) + int(self.L8_2.text())))
            except:
                self.L8_2.setText(str(p[73 + 1]))

            try:
                self.L8_3.setText(str(float(p[74 + 1]) + float(self.L8_3.text())))
            except:
                self.L8_3.setText(str(p[74 + 1]))

            try:
                self.L8_4.setText(str(float(p[75 + 1]) + float(self.L8_4.text())))
            except:
                self.L8_4.setText(str(p[75 + 1]))

            try:
                self.L8_5.setText(str(float(p[76 + 1]) + float(self.L8_5.text())))
            except:
                self.L8_5.setText(str(p[76 + 1]))

            try:
                self.L8_6.setText(str(float(p[77 + 1]) + float(self.L8_6.text())))
            except:
                self.L8_6.setText(str(p[77 + 1]))

            try:
                self.L8_7.setText(str(float(p[78 + 1]) + float(self.L8_7.text())))
            except:
                self.L8_7.setText(str(p[78 + 1]))

            try:
                self.L8_8.setText(str(float(p[79 + 1]) + float(self.L8_8.text())))
            except:
                self.L8_8.setText(str(p[79 + 1]))
            try:
                self.L8_9.setText(str(float(p[80 + 1]) + float(self.L8_9.text())))
            except:
                self.L8_9.setText(str(p[80 + 1]))




                m = self.lineEdit.text()
            H_ = m[2:].split('+')
            self.lcdNumber.display(len(H_))
            
            ll = u'لايوجد'
            ###############################wiki add ###################
            if  self.L1_12.text() !=  '0' and self.L1_6.text() !=  '0'  and self.L1_3.text() !=  '0':
                self.L1_12.setText('reserv.jpg')
                self.L1_6.setText('reserv.jpg')
                self.L1_11.setText('asima_pour_tout.jpg')
            else:

                self.L1_12.setText(p[40])
                self.L1_6.setText(p[41])
                self.L1_11.setText(p[45])

            if  self.L1_7.text() !=  '0' :
                self.L1_7.setText(ll)
            else :
                self.L1_7.setText(p[46])

            if  self.L1_3.text() !=   '0' :
                self.L1_3.setText(ll)
            else :
                self.L1_3.setText(p[42])

            if  self.L1_4.text() !=   '0' :
                self.L1_4.setText(ll)
            else :
                self.L1_4.setText(p[43])

            if self.L1_5.text() !=   '0' :
                self.L1_5.setText(ll)
            else :
                self.L1_5.setText(p[44])
            ##################################################
            if self.L1_8.text() !=  '0' :
                if self.L1_8.text() !=  u'م.غ'  and self.L1_8.text() != '' and p[47] != u'م.غ' :

                    self.L1_8.setText(str(float((float(self.L1_8.text())+ float( unicode(p[47])))/2)))
                else :
                    self.L1_8.setText(ll)
            else :
                self.L1_8.setText(p[47])
            ##################################################
            if self.L1_9.text() != '0' :
                if self.L1_9.text() !=  u'م.غ' and p[48] != u'م.غ'  :
                    self.L1_9.setText(str(float((float(self.L1_9.text())+ float(p[48]))/2)))
                else :
                    self.L1_9.setText(ll)
            else :

                self.L1_9.setText(p[48])
            ################################################


            ################################################

            ###############################################


            #################################################

            #self.L1_9.setText(str(float((float(self.L1_9.text())+ float(p[48]))/2)))
            
            if self.L1_10.text() != '0' :
                self.L1_10.setText(ll)
            else :
                self.L1_10.setText(p[49])

            if self.L2_1.text() != '0' :
                self.L2_1.setText(ll)
            else :
                self.L2_1.setText(p[50])

            if  self.L2_2.text() != '0' :
                self.L2_2.setText(ll)
            else :
                self.L2_2.setText(p[51])

            if  self.L2_3.text() != '0' :
                self.L2_3.setText(ll)
            else :
                self.L2_3.setText(p[52])

            if self.L2_4.text() != '0':
                self.L2_4.setText(ll)
            else :
                self.L2_4.setText(p[53])
            if self.L2_5.text() != '0':
                self.L2_5.setText(ll)
                #str(float(self.L2_5.text()) + float(p[54]))
            else :
                self.L2_5.setText(p[54])
            if self.L2_6.text() != '0':
                self.L2_6.setText(str(int(float(self.L2_6.text()) + float(p[55]))))
            else :
                self.L2_6.setText(p[55])
            if self.L2_7.text() != '0':
                self.L2_7.setText(str(float(float(self.L2_7.text()) + float(p[56]))))
                #str(int(self.L2_7.text()) + int(p[56]))
            else :
                self.L2_7.setText(p[56])
            if self.L2_8.text() != '0':
                self.L2_8.setText(str(float(float(self.L2_8.text()) + float(p[57]))/2))
            else :
                self.L2_8.setText(p[57])
            ###########################################################
            if  self.L2_9.text() != '0' :
                if self.L2_9.text() != u'م.غ' and p[58] !=  u'م.غ' :
                    self.L2_9.setText(str(float((float(self.L2_9.text()) + float(p[58])) / 2)))
                else :
                    self.L2_9.setText(ll)
            else :
                self.L2_9.setText(p[58])
            ##################################################################
            if self.L2_10.text() != '0' :
                if self.L2_10.text() != u'م.غ' and p[59] != u'م.غ'  :
                    self.L2_10.setText(str(float((float(self.L2_10.text()) + float(p[59])) / 2)))
                else :
                    self.L2_10.setText(ll)
            else :
                self.L2_10.setText(p[59])
            ##########################################################
            if  self.L6_9.text() != '0' :

                if self.L6_9.text() != u'م.غ' and p[60] != u'م.غ' :
                    self.L6_9.setText(str(float((float(self.L6_9.text()) + float(p[60])) / 2)))
                else :
                    self.L6_9.setText(ll)
            else :
                self.L6_9.setText(p[60])

            self.L6_10.setText(ll)








            ##### wikibidia #####
            image_map = self.L1_12.text()
            image_embdad = self.L1_6.text()
            embadad = self.L1_3.text()
            tasis = self.L1_4.text()
            asima = self.L1_5.text()
            image_asima = self.L1_11.text()
            tasmiat_sokan = self.L1_7.text()
            katafa = self.L1_8.text()
            motawasit_omr = self.L1_9.text()
            sen_9anoni = self.L1_10.text()
            nidam_hokm = self.L2_1.text()
            rais = self.L2_2.text()
            longage = self.L2_3.text()
            omla = self.L2_4.text()
            jihat_sir = self.L2_5.text()
            nateg_mahali_ij = self.L2_6.text()
            nateg_mahali_fr = self.L2_7.text()
            doal_alam = self.L2_8.text()
            moachir_tanmia = self.L2_9.text()
            moadal_batala = self.L2_10.text()
            nisbat_miah = self.L6_9.text()
            # nisbat_miah = self.L6_9.text()
            add_horob = self.L6_10.text()

            ######################













    def demare(self):
        self.line1.setText('0')
        self.line2.setText('0')
        self.line3.setText('0')
        self.line4.setText('0')
        self.line5.setText('0')
        self.line6.setText('0')
        self.line7.setText('0')
        self.line8.setText('0')
        self.line9.setText('0')
        self.line10.setText('0')
        self.line11.setText('0')
        self.line12.setText('0')
        self.line13.setText('0')
        self.line14.setText('0')
        self.line15.setText('0')
        self.line16.setText('0')
        self.line17.setText('0')
        self.line18.setText('0')
        self.line19.setText('0')
        self.line20.setText('0')
        self.line21.setText('0')
        self.line22.setText('0')
        self.line23.setText('0')
        self.line24.setText('0')
        self.line25.setText('0')
        self.line26.setText('0')
        self.line27.setText('0')
        self.line29.setText('0')
        self.lineEdit.setText('')
        self.lcdNumber.display(0)
        f = self.comboBox.currentText()
        self.line30.setText(str(f))
        self.line31.setText('0')
        self.line32.setText('0')
        self.line33.setText('0')
        self.line34.setText('0')
        self.line35.setText('0')
        self.line36.setText('0')
        self.line37.setText('0')
        self.line38.setText('0')
        self.line39.setText('0')
        self.line40.setText('0')
        self.line41.setText('0')
        ##### wikibidia #####
        self.L1_3.setText('0')
        self.L1_4.setText('0')
        self.L1_5.setText('0')
        self.L1_7.setText('0')
        self.L1_8.setText('0')
        self.L1_9.setText('0')
        self.L1_10.setText('0')
        self.L2_1.setText('0')
        self.L2_2.setText('0')
        self.L2_3.setText('0')
        self.L2_4.setText('0')
        self.L2_5.setText('0')
        self.L2_6.setText('0')
        self.L2_7.setText('0')
        self.L2_8.setText('0')
        self.L2_9.setText('0')
        self.L2_10.setText('0')
        self.L6_9.setText('0')
        self.L1_11.setText('0')
        self.L1_12.setText('0')
        self.L1_6.setText('0')


        #### UNdata
        self.L7_0.setText('0')
        self.L7_1.setText('0')
        self.L7_2.setText('0')
        self.L7_3.setText('0')
        self.L7_4.setText('0')
        self.L7_5.setText('0')
        self.L7_6.setText('0')
        self.L7_7.setText('0')
        self.L7_8.setText('0')
        self.L7_9.setText('0')
        self.L8_0.setText('0')
        self.L8_1.setText('0')
        self.L8_2.setText('0')
        self.L8_3.setText('0')
        self.L8_4.setText('0')
        self.L8_5.setText('0')
        self.L8_6.setText('0')
        self.L8_7.setText('0')
        self.L8_8.setText('0')
        self.L8_9.setText('0')

        ###################################  كل شي هنا من اجل  اوتو كومبليت#####################""


    def auto_(self):
        pass



    def Auto_complete(self,model):
        list_pays = []
        sql = ''' SELECT * FROM table_1 '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for e in data:
            l = e[28]
            list_pays.append(str(l))



        model.setStringList(list_pays)

    def line(self):
        a = self.lineEdit_3
        completer = QCompleter()
        a.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_complete(model)

    def hhhh(self):
        f = self.lineEdit_3.text()
        K = []
        sql = ''' SELECT * FROM table_1 '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for e in data:
            l = e[28]
            K.append(str(l))
        g = K.index(str(f))
        self.comboBox.setCurrentIndex(g)
        #print t

    def vers_cod_creat_video(self):
        ## val slide 0 #################
        if self.target_vargul == True :

            valeur_stat_slid0_1 = [self.L1_10.text(),self.L1_9.text(),self.L1_8.text(),self.L1_7.text(),self.line29.text(),
                  self.L1_5.text(),self.L1_4.text(),self.L1_3.text(),self.L1_2.text(),self.line30.text()]

            valeur_stat_slid0_2 = [self.L1_10.text(),self.L1_9.text(),self.L1_8.text(),self.L1_7.text(),self.line29.text(),
                  self.L1_5.text(),self.L1_4.text(),self.L1_3.text(),self.L1_2.text(),self.line30.text()]


            ## val slide 1 #################
            valeur_stat_slid1_1 = [self.L2_10.text(), self.L2_9.text(), self.L2_8.text(),
                                   self.L2_7.text(), self.L2_6.text(),
                                   self.L2_5.text(), self.L2_4.text(), self.L2_3.text(),
                                   self.L2_2.text(), self.L2_1.text()]

            valeur_stat_slid1_2 = [self.L2_10.text(), self.L2_9.text(), self.L2_8.text(),
                                   self.L2_7.text(), self.L2_6.text(),
                                   self.L2_5.text(), self.L2_4.text(), self.L2_3.text(),
                                   self.L2_2.text(), self.L2_1.text()]

            ## val slide 2 #################
            valeur_stat_slid2_1 = [self.line19.text(), self.line20.text(),self.line21.text(),
                                   self.line22.text(), self.line23.text(),
                                   self.line24.text(), self.line25.text(), self.line26.text(),
                                   self.line27.text(), self.line31.text()]


            valeur_stat_slid2_2 = [self.line19.text(), self.line20.text(),self.line21.text(),
                                   self.line22.text(), self.line23.text(),
                                   self.line24.text(), self.line25.text(), self.line26.text(),
                                   self.line27.text(), self.line31.text()]



            ## val slide 3 #################
            valeur_stat_slid3_1 = [self.line9.text(), self.line10.text(), self.line11.text(),
                                   self.line12.text(), self.line13.text(),
                                   self.line14.text(), self.line15.text(), self.line16.text(),
                                   self.line17.text(), self.line18.text()]


            valeur_stat_slid3_2 = [self.line9.text(), self.line10.text(), self.line11.text(),
                                   self.line12.text(), self.line13.text(),
                                   self.line14.text(), self.line15.text(), self.line16.text(),
                                   self.line17.text(), self.line18.text()]
            ############################################ slide  4

            valeur_stat_slid4_1 = [self.line38.text(), self.line39.text(), self.line40.text(),
                                   self.line41.text(), self.line3.text(),
                                   self.line4.text(), self.line5.text(), self.line6.text(),
                                   self.line7.text(), self.line8.text()]

            valeur_stat_slid4_2 = [self.line38.text(), self.line39.text(), self.line40.text(),
                                   self.line41.text(), self.line3.text(),
                                   self.line4.text(), self.line5.text(), self.line6.text(),
                                   self.line7.text(), self.line8.text()]
            ########################################## slide 5
            valeur_stat_slid5_1 =  [self.L6_10.text(), self.L6_9.text(), self.line2.text(),
                                   self.line1.text(), self.line32.text(),
                                   self.line33.text(), self.line34.text(), self.line35.text(),
                                   self.line36.text(), self.line37.text()]

            valeur_stat_slid5_2 = [self.L6_10.text(), self.L6_9.text(), self.line2.text(),
                                   self.line1.text(), self.line32.text(),
                                   self.line33.text(), self.line34.text(), self.line35.text(),
                                   self.line36.text(), self.line37.text()]
            ########################################## slide 6
            valeur_stat_slid6_1 = [self.L7_0.text(), self.L7_1.text(), self.L7_2.text(),
                                   self.L7_3.text(), self.L7_4.text(),
                                   self.L7_5.text(), self.L7_6.text(), self.L7_7.text(),
                                   self.L7_8.text(), self.L7_9.text()]

            valeur_stat_slid6_2 = [self.L7_0.text(), self.L7_1.text(), self.L7_2.text(),
                                   self.L7_3.text(), self.L7_4.text(),
                                   self.L7_5.text(), self.L7_6.text(), self.L7_7.text(),
                                   self.L7_8.text(), self.L7_9.text()]
            ########################################## slide 7
            valeur_stat_slid7_1 = [self.L8_0.text(), self.L8_1.text(), self.L8_2.text(),
                                   self.L8_3.text(), self.L8_4.text(),
                                   self.L8_5.text(), self.L8_6.text(), self.L8_7.text(),
                                   self.L8_8.text(), self.L8_9.text()]

            valeur_stat_slid7_2 =  [self.L8_0.text(), self.L8_1.text(), self.L8_2.text(),
                                   self.L8_3.text(), self.L8_4.text(),
                                   self.L8_5.text(), self.L8_6.text(), self.L8_7.text(),
                                   self.L8_8.text(), self.L8_9.text()]
            #print len(valeur_stat_slid0_1)
            f1 = ['10001','10002','100003','100004','10000005','100006','100007','100008','100009','hemidi']
            # data from site data un

            valeur_data7_1 =  []
            valeur_data7_2 =  []
            valeur_data8_1 =  []
            valeur_data8_2 =  []
            valeur_data9_1 =  []
            valeur_data9_2 =  []
            valeur_data10_1 = []
            valeur_data10_2 = []



            ##################### link image ####################

            img_1 = self.lineEdit_4.text()
            img_2 = self.lineEdit_5.text()
            image_as = self.L1_11.text()
            image_embdad = self.L1_6.text()
            image_map = self.L1_12.text()
            #image_as = self.L1_11.text()



            k = 0
            slide_1_1 = 1
            slide_0_0 = 1

            if  self.radioButton.isChecked() and img_1 != '' :
                slide_0_0 = None
                image =  img_1
            elif  self.radioButton_2.isChecked() and img_2 != '' :
                slide_1_1 = None
                image =  img_2
            else :
                k = 1
            if k == 0 :
                m = creat_video()


                m.ajouter_text(valeur_stat_slid0_1, valeur_stat_slid0_2 , valeur_stat_slid1_1,
                               valeur_stat_slid1_2,valeur_stat_slid2_1,valeur_stat_slid2_2,
                               valeur_stat_slid3_1,valeur_stat_slid3_2,slide_0_0,slide_1_1,image,valeur_stat_slid4_1,valeur_stat_slid4_2,
                               valeur_stat_slid5_1,valeur_stat_slid5_2,image_as , image_embdad,image_map ,valeur_stat_slid6_1,valeur_stat_slid6_2,
                               valeur_stat_slid7_1 , valeur_stat_slid7_2)
                Qt.QMessageBox.information(self, u'صحيت', u'تم ')

                self.target_vargul = False
            else :
                Qt.QMessageBox.critical(self, u'خطأ', u'مشكل في رابط الصوة او البوطون راديو')
        else:
            Qt.QMessageBox.critical(self, u'خطأ', u'نسيت الفاصلة')

    ################################ calculer comparinge contraiy

    def clacu_l_comparing(self):
        # هذي الدالة فقط للعمل مع الحساب الاخير بش ندير مقارنة بين الدول ملخص المقارنة في الاخير
        valeur_stat_slid0_1 = [str(self.L1_10.text()), str(unicode(self.L1_9.text())), str(unicode(self.L1_8.text())), str(unicode(self.L1_7.text())),
                               str(unicode(self.line29.text())),
                               str(unicode(self.L1_5.text())), str(unicode(self.L1_4.text())), str(unicode(self.L1_3.text())), str(unicode(self.L1_2.text())),
                               str(unicode(self.line30.text()))]


        valeur_stat_slid0_2 = [str(self.L1_10.text()), str(self.L1_9.text()), str(self.L1_8.text()), str(self.L1_7.text()),
                               str(self.line29.text()),
                               str(self.L1_5.text()), str(self.L1_4.text()), str(self.L1_3.text()), str(self.L1_2.text()),
                               str(self.line30.text())]

        ## val slide 1 #################
        valeur_stat_slid1_1 = [str(self.L2_10.text()), str(self.L2_9.text()), str(self.L2_8.text()),
                               str(self.L2_7.text()), str(self.L2_6.text()),
                               str(self.L2_5.text()), str(self.L2_4.text()), str(self.L2_3.text()),
                               str(self.L2_2.text()), str(self.L2_1.text())]

        valeur_stat_slid1_2 = [str(self.L2_10.text()), str(self.L2_9.text()), str(self.L2_8.text()),
                               str(self.L2_7.text()), str(self.L2_6.text()),
                               str(self.L2_5.text()), str(self.L2_4.text()), str(self.L2_3.text()),
                               str(self.L2_2.text()), str(self.L2_1.text())]

        ## val slide 2 #################
        valeur_stat_slid2_1 = [str(self.line19.text()), str(self.line20.text()), str(self.line21.text()),
                               str(self.line22.text()), str(self.line23.text()),
                               str(self.line24.text()), str(self.line25.text()), str(self.line26.text()),
                               str(self.line27.text()), str(self.line31.text())]

        valeur_stat_slid2_2 = [str(self.line19.text()), str(self.line20.text()), str(self.line21.text()),
                               str(self.line22.text()), str(self.line23.text()),
                               str(self.line24.text()), str(self.line25.text()), str(self.line26.text()),
                               str(self.line27.text()), str(self.line31.text())]

        ## val slide 3 #################
        valeur_stat_slid3_1 = [str(self.line9.text()), str(self.line10.text()), str(self.line11.text()),
                               str(self.line12.text()), str(self.line13.text()),
                               str(self.line14.text()), str(self.line15.text()), str(self.line16.text()),
                               str(self.line17.text()), str(self.line18.text())]

        valeur_stat_slid3_2 = [str(self.line9.text()), str(self.line10.text()), str(self.line11.text()),
                               str(self.line12.text()), str(self.line13.text()),
                               str(self.line14.text()), str(self.line15.text()), str(self.line16.text()),
                               str(self.line17.text()), str(self.line18.text())]
        ############################################ slide  4

        valeur_stat_slid4_1 = [str(self.line38.text()), str(self.line39.text()), str(self.line40.text()),
                               str(self.line41.text()), str(self.line3.text()),
                               str(self.line4.text()), str(self.line5.text()), str(self.line6.text()),
                               str(self.line7.text()), str(self.line8.text())]

        valeur_stat_slid4_2 = [str(self.line38.text()), str(self.line39.text()), str(self.line40.text()),
                               str(self.line41.text()), str(self.line3.text()),
                               str(self.line4.text()), str(self.line5.text()), str(self.line6.text()),
                               str(self.line7.text()), str(self.line8.text())]

        ########################################## slide 5
        valeur_stat_slid5_1 = [str(self.L6_10.text()), str(self.L6_9.text()), str(self.line2.text()),
                               str(self.line1.text()), str(self.line32.text()),
                               str(self.line33.text()), str(self.line34.text()), str(self.line35.text()),
                               str(self.line36.text()), str(self.line37.text())]

        valeur_stat_slid5_2 = [str(self.L6_10.text()), str(self.L6_9.text()), str(self.line2.text()),
                               str(self.line1.text()), str(self.line32.text()),
                               str(self.line33.text()), str(self.line34.text()), str(self.line35.text()),
                               str(self.line36.text()), str(self.line37.text())]

        ##################### link image ####################

        img_1 = self.lineEdit_4.text()
        img_2 = self.lineEdit_5.text()
        image_as = self.L1_11.text()
        image_embdad = self.L1_6.text()
        image_map = self.L1_12.text()
        # image_as = self.L1_11.text()

        k = 0
        slide_1_1 = 1
        slide_0_0 = 1

        if self.radioButton.isChecked() and img_1 != '':
            slide_0_0 = None
            image = img_1
        elif self.radioButton_2.isChecked() and img_2 != '':
            slide_1_1 = None
            image = img_2
        contry1 =[]
        contry2=[]

        if self.radioButton.isChecked() :
            contry1 = (valeur_stat_slid0_1 , valeur_stat_slid1_1,valeur_stat_slid2_1,valeur_stat_slid3_1,valeur_stat_slid4_1,valeur_stat_slid5_1,str(image))
            f = open('stor.bin', 'w')
            dump((contry1), f)
            f.close()
        if self.radioButton_2.isChecked():
            contry2 = (valeur_stat_slid0_2, valeur_stat_slid1_2, valeur_stat_slid2_2, valeur_stat_slid3_2,
                               valeur_stat_slid4_2, valeur_stat_slid5_2, str(image))
            l = open('stor2.bin', 'w')
            dump((contry2), l)
            l.close()
        #if contry2 != [] and contry1 != [] :

        #if contry1 != [] and contry2 != [] :

        #for i in contry2 :
        #    print(i)
        #print(contry1)
        #print('****************************************************************************')
        #print(contry2)
    def calcul_staus_appal(self):
        try:
            calcul_status.result()
            Qt.QMessageBox.information(self, u'صحيت', u'تم التعديل بنجاح شكرا سي بن عامر')
        except :
            Qt.QMessageBox.critical(self, u'خطأ', u'مشكل ')


    ################### vers link images ####################################
    def open_img_1(self):

        save__ =  Qt.QFileDialog.getOpenFileName(self,caption = 'select img' , directory = "F:/TA9AFA ASKARYA/flag" , filter = 'AU filles(*.*)')
        self.lineEdit_4.setText(save__)



    def open_img_2(self):

        save__ =  Qt.QFileDialog.getOpenFileName(self,caption = 'select img' , directory = "F:/TA9AFA ASKARYA/flag" , filter = 'AU filles(*.*)')

        self.lineEdit_5.setText(save__)

    def open_img_map(self):
        save__ = Qt.QFileDialog.getOpenFileName(self, caption='select img', directory="C:/Users/benam/OneDrive/Bureau/cod python ppt/map",
                                                filter='AU filles(*.*)')

        self.L1_12.setText(save__)

    def open_imag_as(self):

        save__ = Qt.QFileDialog.getOpenFileName(self, caption='select img', directory="C:/Users/benam/OneDrive/Bureau/cod python ppt/asima",
                                                filter='AU filles(*.*)')

        self.L1_11.setText(save__)
    def open_img_embad(self):
        save__ = Qt.QFileDialog.getOpenFileName(self, caption='select img', directory="C:/Users/benam/OneDrive/Bureau/cod python ppt/embadad",
                                                filter='AU filles(*.*)')

        self.L1_6.setText(save__)

    def save_fille(self):
        l = creat_video()
        l.save_fiile()
        Qt.QMessageBox.information(self, u'صحيت', u'تم')




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()

    from shutil import copyfile

    copyfile('hemidi_hemidi.pptx', 'hemidi.pptx')

    window.show()
    sys.exit(app.exec_())
