import gelen_veriyi_duzenleme
import database
Karsilastirilmis_liste=[["" for i in range(3)] for j in range(1200000)]
a=0
def karsilastirma_bulma(tablo_adi):
        duzenlenmis_liste=gelen_veriyi_duzenleme.veri_duzenleme(tablo_adi)
        for k in range(0,29):#len(duzenlenmis_liste)-1
            #alinan cumle icin diger tum cumlelerin alinmasi.
            for karsilastir in range(k+1,30):#len(duzenlenmis_liste)
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
                Karsilastirilmis_liste[a][1]=veri1
                Karsilastirilmis_liste[a][2]=veri2
                Karsilastirilmis_liste[a][3]=benzerlik
                a+=1
                #database.karsilastirma_verisi_ekle(veri1,veri2,benzerlik,tablo_adi)