import database
def veri_duzenleme(tablo_adi,ID):
    if ID=="0":
        list_veriler = database.veri_okuma(tablo_adi)
        duzenlenmis_liste =[]
        for satir in list_veriler:
            for cumle in satir:
                parcalanmis_cumle=cumle.split(" ")
                yeni_cumle=[]
                for kelime in parcalanmis_cumle:
                    if kelime!='':
                        yeni_cumle.append(kelime)
                duzenlenmis_liste.append(yeni_cumle)
        return duzenlenmis_liste
    else:
            list_veriler = database.ID_oku(tablo_adi,ID)
            duzenlenmis_liste =[]
            for satir in list_veriler:
                for cumle in satir:
                    parcalanmis_cumle=cumle.split(" ")
                    yeni_cumle=[]
                    for kelime in parcalanmis_cumle:
                        if kelime!='':
                            yeni_cumle.append(kelime)
                    duzenlenmis_liste.append(yeni_cumle)
            return duzenlenmis_liste

def veri_duzenleme_product(tablo_adi,girilen_product):
        list_veriler,list_sirketler = database.gelen_product_oku(tablo_adi,girilen_product)
        duzenlenmis_liste =[]
        for satir in list_veriler:
            for cumle in satir:
                parcalanmis_cumle=cumle.split(" ")
                yeni_cumle=[]
                for kelime in parcalanmis_cumle:
                    if kelime!='':
                        yeni_cumle.append(kelime)
                duzenlenmis_liste.append(yeni_cumle)

        duzenlenmis_liste_sirketler =[]
        for satir in list_sirketler:
            for cumle in satir:
                parcalanmis_cumle=cumle.split(" ")
                yeni_cumle=[]
                for kelime in parcalanmis_cumle:
                    if kelime!='':
                        yeni_cumle.append(kelime)
                duzenlenmis_liste_sirketler.append(yeni_cumle)
        return duzenlenmis_liste,duzenlenmis_liste_sirketler