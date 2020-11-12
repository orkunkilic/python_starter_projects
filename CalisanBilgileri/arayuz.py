import olustur,arama,silme

while True:

    print("====================VERİTABANI YÖNETİM MERKEZİ====================\n\n")
    secenek=input("1-Veritabanına çalışan ekleme\n2-Veritabanında çalışan arama\n3-Veritabanından çalışan silme\n==>>")

    if(secenek=="1"):
        olustur.main()
    elif(secenek=="2"):
        arama.main()
    elif(secenek=="3"):
        silme.main()
    else:
        print("Hatalı giriş!")