def main():

    import sqlite3

    class calisan:
        def tc(self,tc):
            global calisantc
            calisantc=tc

        def ad(self,ad):
            global calisanad
            calisanad=ad

        def soyad(self,soyad):
            global calisansoyad
            calisansoyad=soyad

        def maas(self,maas):
            global calisanmaas
            calisanmaas=maas

        def bolum(self,bolum):
            global calisanbolum
            calisanbolum=bolum

    def ekle(tc,ad,soyad,maas,bolum):
        baglanti = sqlite3.connect('database.db')
        veritabani_sec = baglanti.cursor()
        params=(tc,ad,soyad,maas,bolum)
        veritabani_sec.execute("INSERT INTO calisan VALUES (NULL,?,?,?,?,?)",params)
        baglanti.commit()
        baglanti.close()


    tc=input("Tc giriniz:")
    ad=input("Ad giriniz:")
    soyad=input("Soyad giriniz:")
    maas=input("Maaş giriniz:")
    bolum=input("Bölüm giriniz:")

    calisan=calisan()
    calisan.tc(tc)
    calisan.ad(ad)
    calisan.soyad(soyad)
    calisan.maas(maas)
    calisan.bolum(bolum)
    ekle(calisantc,calisanad,calisansoyad,calisanmaas,calisanbolum)


