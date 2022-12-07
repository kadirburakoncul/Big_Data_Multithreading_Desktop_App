#pip install PyQt5
from ast import Index
import enum
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from panel import*
import karsilastirma
import threading
import time


import gelen_veriyi_duzenleme
import database


uygulama= QApplication(sys.argv)
pencere=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

def karsilastirma_dongu(girilen_ID,girilen_product,tablo_adi,istenilen_benzerlik_orani,baslangic,bitis,duzenlenmis_liste,duzenlenmis_liste2,duzenlenmis_liste_sirketler,girilen_son_deger,i):
    if girilen_ID=="0" and girilen_product=="0":
        a=0
        for k in range(baslangic,bitis):#len(duzenlenmis_liste)-1
            #alinan cumle icin diger tum cumlelerin alinmasi.
            for karsilastir in range(k+1,girilen_son_deger):#len(duzenlenmis_liste)
                print("thread degeri= {} , ilk Sıralama : {} , ikinci Sıralama : {} ".format(i,k,karsilastir))
                var=0
                en_uzun_olan_cumle=0
                #kelimeler tek tek aliniyor karsilastirma icin.
                for kelime_indeks in range(0,len(duzenlenmis_liste[k])):
                    #karsilastirilan cumle icerisinde tek kelime dolasiyor.
                    for karsilastir_kelime_indeks in range(0,len(duzenlenmis_liste[karsilastir])):
                        varmi=duzenlenmis_liste[karsilastir][karsilastir_kelime_indeks].find(duzenlenmis_liste[k][kelime_indeks])
                        if varmi==0:
                            var+=1
                if len(duzenlenmis_liste[k])>=len(duzenlenmis_liste[karsilastir]):
                    en_uzun_olan_cumle=len(duzenlenmis_liste[k])
                else:
                    en_uzun_olan_cumle=len(duzenlenmis_liste[karsilastir])
                veri1=""
                veri2=""
                for kelime in duzenlenmis_liste[k]:
                    veri1+=kelime
                    veri1+=" "
                for kelime in duzenlenmis_liste[karsilastir]:
                    veri2+=kelime
                    veri2+=" "
                benzerlik=(var*100)/en_uzun_olan_cumle
                benzerlik_str=str(benzerlik)
                if float(istenilen_benzerlik_orani)<= benzerlik:
                    ui.Table1.setItem(a,0,QtWidgets.QTableWidgetItem(veri1))
                    ui.Table1.setItem(a,1,QtWidgets.QTableWidgetItem(veri2))
                    ui.Table1.setItem(a,2,QtWidgets.QTableWidgetItem(benzerlik_str))
                    a+=1
    elif girilen_ID!="0":
        a=0
            #alinan cumle icin diger tum cumlelerin alinmasi.
        for karsilastir in range(baslangic,bitis):#len(duzenlenmis_liste)
                print("thread degeri= {} , Sıralama : {}".format(i,karsilastir))
                var=0
                en_uzun_olan_cumle=0
                #kelimeler tek tek aliniyor karsilastirma icin.
                for kelime_indeks in range(0,len(duzenlenmis_liste[0])):
                    #karsilastirilan cumle icerisinde tek kelime dolasiyor.
                    for karsilastir_kelime_indeks in range(0,len(duzenlenmis_liste2[karsilastir])):
                        varmi=duzenlenmis_liste2[karsilastir][karsilastir_kelime_indeks].find(duzenlenmis_liste[0][kelime_indeks])
                        if varmi==0:
                            var+=1
                if len(duzenlenmis_liste[0])>=len(duzenlenmis_liste2[karsilastir]):
                    en_uzun_olan_cumle=len(duzenlenmis_liste[0])
                else:
                    en_uzun_olan_cumle=len(duzenlenmis_liste2[karsilastir])
                veri1=""
                veri2=""
                for kelime in duzenlenmis_liste[0]:
                    veri1+=kelime
                    veri1+=" "
                for kelime in duzenlenmis_liste2[karsilastir]:
                    veri2+=kelime
                    veri2+=" "
                benzerlik=(var*100)/en_uzun_olan_cumle
                benzerlik_str=str(benzerlik)
                if float(istenilen_benzerlik_orani)<= benzerlik:
                    ui.Table1.setItem(a,0,QtWidgets.QTableWidgetItem(veri1))
                    ui.Table1.setItem(a,1,QtWidgets.QTableWidgetItem(veri2))
                    ui.Table1.setItem(a,2,QtWidgets.QTableWidgetItem(benzerlik_str))
                    a+=1
    elif girilen_product!="0":
        a=0
        for k in range(baslangic,bitis):#len(duzenlenmis_liste)-1
            #alinan cumle icin diger tum cumlelerin alinmasi.
            for karsilastir in range(k+1,girilen_son_deger):#len(duzenlenmis_liste)
                print("thread degeri= {} , ilk Sıralama : {} , ikinci Sıralama : {} ".format(i,k,karsilastir))
                var=0
                en_uzun_olan_cumle=0
                #kelimeler tek tek aliniyor karsilastirma icin.
                for kelime_indeks in range(0,len(duzenlenmis_liste[k])):
                    #karsilastirilan cumle icerisinde tek kelime dolasiyor.
                    for karsilastir_kelime_indeks in range(0,len(duzenlenmis_liste[karsilastir])):
                        varmi=duzenlenmis_liste[karsilastir][karsilastir_kelime_indeks].find(duzenlenmis_liste[k][kelime_indeks])
                        if varmi==0:
                            var+=1
                if len(duzenlenmis_liste[k])>=len(duzenlenmis_liste[karsilastir]):
                    en_uzun_olan_cumle=len(duzenlenmis_liste[k])
                else:
                    en_uzun_olan_cumle=len(duzenlenmis_liste[karsilastir])
                veri1=""
                veri2=""
                sirket1=""
                sirket2=""
                for kelime in duzenlenmis_liste[k]:
                    veri1+=kelime
                    veri1+=" "
                for kelime in duzenlenmis_liste[karsilastir]:
                    veri2+=kelime
                    veri2+=" "
                benzerlik=(var*100)/en_uzun_olan_cumle
                benzerlik_str=str(benzerlik)
                if float(istenilen_benzerlik_orani)<= benzerlik:
                    ui.Table1.setItem(a,0,QtWidgets.QTableWidgetItem(veri1))
                    ui.Table1.setItem(a,1,QtWidgets.QTableWidgetItem(veri2))
                    ui.Table1.setItem(a,2,QtWidgets.QTableWidgetItem(benzerlik_str))
                    for kelime in duzenlenmis_liste_sirketler[k]:
                        sirket1+=kelime
                        sirket1+=" "
                    for kelime in duzenlenmis_liste_sirketler[karsilastir]:
                        sirket2+=kelime
                        sirket2+=" "
                    ui.Table1.setItem(a,3,QtWidgets.QTableWidgetItem(sirket1))
                    ui.Table1.setItem(a,4,QtWidgets.QTableWidgetItem(sirket2))
                    ui.Table1.setItem(a,5,QtWidgets.QTableWidgetItem(girilen_product))
                    a+=1

def karsilastirma_bulma():
        ui.Table1.clear()
        ui.Table1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        ui.Table1.setHorizontalHeaderLabels(("Kayıt 1","Kayıt 2","Benzerlik Oranı","Şirket 1","Şirket 2","Product"))
        tablo_adi=ui.comboBox_tablo_adi.currentText()
        istenilen_benzerlik_orani=ui.comboBox_oran.currentText()
        girilen_ID=ui.lineEdit_ID.text()
        girilen_product=ui.lineEdit_Product_Isim.text()
        girilen_thread_sayisi=int(ui.lineEdit_Thread_Sayisi.text())
        girilen_son_deger=int(ui.lineEdit_Son_Deger.text())
        duzenlenmis_liste2=[]
        duzenlenmis_liste_sirketler=[]
        if girilen_ID=="0" and girilen_product=="0":
            duzenlenmis_liste=gelen_veriyi_duzenleme.veri_duzenleme(tablo_adi,"0")
            #thread_araligi=int((len(duzenlenmis_liste)-1)/girilen_thread_sayisi)
            thread_araligi=int(girilen_son_deger/girilen_thread_sayisi)
        elif girilen_ID!="0":
            duzenlenmis_liste=gelen_veriyi_duzenleme.veri_duzenleme(tablo_adi,girilen_ID)
            duzenlenmis_liste2=gelen_veriyi_duzenleme.veri_duzenleme(tablo_adi,"0")
            #thread_araligi=int((len(duzenlenmis_liste2)-1)/girilen_thread_sayisi)
            thread_araligi=int(girilen_son_deger/girilen_thread_sayisi)
        elif girilen_product!="0":
            duzenlenmis_liste,duzenlenmis_liste_sirketler=gelen_veriyi_duzenleme.veri_duzenleme_product(tablo_adi,girilen_product)
            duzenlenmis_liste=gelen_veriyi_duzenleme.veri_duzenleme(tablo_adi,"0")
            #thread_araligi=int((len(duzenlenmis_liste2)-1)/girilen_thread_sayisi)
            thread_araligi=int(girilen_son_deger/girilen_thread_sayisi)

        threads = []
        for i in range(0,girilen_thread_sayisi):
            if i==0:
                t = threading.Thread(target=karsilastirma_dongu,args = (girilen_ID,girilen_product,tablo_adi,istenilen_benzerlik_orani,1,thread_araligi,duzenlenmis_liste,duzenlenmis_liste2,duzenlenmis_liste_sirketler,girilen_son_deger,i))
            elif i==1:
                t = threading.Thread(target=karsilastirma_dongu,args = (girilen_ID,girilen_product,tablo_adi,istenilen_benzerlik_orani,thread_araligi,2*thread_araligi,duzenlenmis_liste,duzenlenmis_liste2,duzenlenmis_liste_sirketler,girilen_son_deger,i))
            else:
                t = threading.Thread(target=karsilastirma_dongu,args = (girilen_ID,girilen_product,tablo_adi,istenilen_benzerlik_orani,i*thread_araligi,(i+1)*thread_araligi,duzenlenmis_liste,duzenlenmis_liste2,duzenlenmis_liste_sirketler,girilen_son_deger,i))
            print("thread = {}".format(i))
            t.start()
            threads.append(t)
        #karsilastirma_dongu(girilen_ID,girilen_product,tablo_adi,istenilen_benzerlik_orani)



ui.pushButton_karsilastir.clicked.connect(karsilastirma_bulma)


sys.exit(uygulama.exec_())
