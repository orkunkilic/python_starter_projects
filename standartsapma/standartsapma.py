liste=[]
def ss(liste):
    toplam = 0

    for a in range(len(liste)):
        toplam=toplam+float(liste[a])
    ortalama=toplam/len(liste)

    a=0
    karetop=0
    for a in range(len(liste)):
        karetop=karetop+((float(liste[a])-ortalama)**2)

    sonuc=(karetop/(len(liste)-1))**(1/2)

    return round(sonuc,3)

for i in range(100):
    a=input("Sayı:")
    if a=="":
        break

    liste.append(a)

print("\n\nStandart Sapma="+str(ss(liste)))