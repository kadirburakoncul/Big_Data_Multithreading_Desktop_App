#pip install pypyodbc
import pypyodbc
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-S1PUR1BJ;'
    'Database=proje;'
    'Trusted_Connection=True;'
)

def kapat():
    db.close()

def veri_ekle(product,issue,company,state,complaint_ID,zip_code):
    imlec=db.cursor()
    imlec.execute("insert into veriler values('{}','{}','{}','{}','{}','{}')".format(product,issue,company,state,complaint_ID,zip_code))
    imlec.commit()

def veri_okuma(tablo_adi):
    list_veriler=[]
    imlec=db.cursor()
    imlec.execute("SELECT {} FROM veriler".format(tablo_adi))
    veriler=imlec.fetchall()
    for k in veriler:
        list_veriler.append(k)
    return list_veriler

def ID_oku(tablo_adi,ID):
    list_veriler=[]
    imlec=db.cursor()
    imlec.execute("SELECT {} FROM veriler WHERE Complaint_ID='{}'".format(tablo_adi,ID))
    veriler=imlec.fetchall()
    for k in veriler:
        list_veriler.append(k)
    return list_veriler

def gelen_product_oku(tablo_adi,girilen_product):
    list_veriler=[]
    imlec=db.cursor()
    imlec.execute("SELECT {} FROM veriler WHERE Product='{}'".format(tablo_adi,girilen_product))
    veriler=imlec.fetchall()
    for k in veriler:
        list_veriler.append(k)

    list_sirketler=[]
    imlec.execute("SELECT {} FROM veriler WHERE Product='{}'".format("Company",girilen_product))
    sirket=imlec.fetchall()
    for k in sirket:
        list_sirketler.append(k)
    return list_veriler,list_sirketler