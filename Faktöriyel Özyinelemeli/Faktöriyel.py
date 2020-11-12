def fak(n):
    if n > 1:
        sonuc = n * fak(n - 1)
    elif n<0:
        sonuc = "Hata"
    else:
        sonuc=1

    return sonuc

n=int(input("Sayıyı Giriniz:"))


print(fak(n))
