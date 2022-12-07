import csv
import database
import symbol_remove
import stopWordRemove
import numpy as np

def listeden_database_veri_cek():
    k=0
    with open('rows.csv', 'r',encoding="utf8") as dosya:
        cvs_oku = csv.reader(dosya, delimiter=',')
        dizi =[[0 for i in range(6)] for j in range(1500000)]
        for satir in cvs_oku:
            if satir[1]!="" and satir[3]!="" and satir[7]!="" and satir[8]!="" and satir[17]!="" and satir[9]!="":
                satir1=symbol_remove.sembol_remove_bulma(satir[1])
                satir3=symbol_remove.sembol_remove_bulma(satir[3])
                satir7=symbol_remove.sembol_remove_bulma(satir[7])
                satir8=symbol_remove.sembol_remove_bulma(satir[8])
                satir17=symbol_remove.sembol_remove_bulma(satir[17])
                satir9=symbol_remove.sembol_remove_bulma(satir[9])
                satir1=stopWordRemove.stopWordRemove_bulma(satir1)
                satir3=stopWordRemove.stopWordRemove_bulma(satir3)
                satir7=stopWordRemove.stopWordRemove_bulma(satir7)
                satir8=stopWordRemove.stopWordRemove_bulma(satir8)
                satir17=stopWordRemove.stopWordRemove_bulma(satir17)
                satir9=stopWordRemove.stopWordRemove_bulma(satir9)
                dizi[k][0]=satir1
                dizi[k][1]=satir3
                dizi[k][2]=satir7
                dizi[k][3]=satir8
                dizi[k][4]=satir17
                dizi[k][5]=satir9
                k+=1
        for satir in dizi: 
            if satir[0]==0:
                break
            else:
                database.veri_ekle(satir[0],satir[1],satir[2],satir[3],satir[4],satir[5])
