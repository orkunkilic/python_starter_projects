import sinifmethodlar
x=sinifmethodlar.Bank()
while True:
    print("\n\n==========A BANK==========")
    giris=input("1-Para çekme 2-Para yatırma 3-Para sorgulama:\n...")
    if(giris=="1"):
        miktar=int(input("Çekmek istediğiniz miktarı giriniz:"))
        x.paracek(miktar)
        print("İşleminiz tamamlandı.Teşekkürler.")
    elif(giris=="2"):
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz:"))
        x.parayatir(miktar)
        print("İşleminiz tamamlandı.Teşekkürler.")
    elif(giris=="3"):
        x.kontrol()
    else:
        print("Hatalı komut.")
