def main():
    import sqlite3


    def search(giris):
        baglanti = sqlite3.connect('database.db')
        veritabani_sec = baglanti.cursor()

        sonuc=veritabani_sec.execute("SELECT * FROM calisan WHERE tc=? OR adi=? OR soyadi=? OR maas=? OR bolum=?",(giris,giris,giris,giris,giris))
        sss=sonuc.fetchall()

        baglanti.close

        if(sss==[]):
            print("Girdiğiniz bilgilere ilişkin sonuç bulunamadı!")

        else:
            print("\nEn alakalı sonuç listelenmektedir!")



            print("\nÇalışan Kimlik Numarası:",sss[0][1])

            print("Çalışan İsmi:",sss[0][2])

            print("Çalışan Soyismi:",sss[0][3])

            print("Çalışan Maaşı:",sss[0][4])

            print("Çalışan Bölümü",sss[0][5])


    giris=input("Aradığınız kişinin herhangi bir bilgisi:")

    search(giris)


