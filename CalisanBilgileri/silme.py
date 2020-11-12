def main():
    import sqlite3
    def delete(giris):
        baglanti = sqlite3.connect('database.db')
        veritabani_sec = baglanti.cursor()

        veritabani_sec.execute("DELETE FROM calisan WHERE tc=?",[giris])
        baglanti.commit()
        baglanti.close()
        print("Çalışan veritabanından silindi!")



    giris=input("Veritabanından silmek istediğiniz kişinin TC Kimlik numarasını giriniz:")
    delete(giris)

