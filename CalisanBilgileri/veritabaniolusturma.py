import sqlite3

baglanti = sqlite3.connect('database.db')
veritabani_sec = baglanti.cursor()

veritabani_sec.execute( '''
CREATE TABLE calisan(
no INTEGER PRIMARY KEY,
tc INTEGER NOT NULL ,
adi VARCHAR(50),
soyadi VARCHAR(50),
maas INTEGER NOT NULL ,
bolum VARCHAR(50)
)
''' )
