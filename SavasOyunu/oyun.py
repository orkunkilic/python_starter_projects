import oyunsinif,random


print("OYUNA HOŞGELDİNİZ!\n")


p1=input("Birinci oyuncunun adı:")
p2=input("İkinci oyuncunun adı:")
a=random.randint(1,2)
if(a==1):
    x=oyunsinif.Player(p1)
    y=oyunsinif.Player(p2)
else:
    c=p1
    p1=p2
    p2=c
    x = oyunsinif.Player(p1)
    y = oyunsinif.Player(p2)
print("\nDefault Can Değeri:200\nDefault Saldırı Gücü Değeri:5\n\n\n")
print("Saldırma(1)\nCan değeri arttırma(2)\nSaldırı gücü arttırma(3)\n")

try:
    input("Başlamak için Enter tuşuna basınız...\n")
except SyntaxError:
    pass

while (y.can>0):
    while (x.can>0):
        print(p1,"adlı kullanıcının sırası:")
        giris1=int(input())
        if(giris1==1):
            y.saldiriugra(x.saldir())
        elif(giris1==2):
            x.canbas()
        elif(giris1==3):
            x.gucartir()
        else:
            print("Hatalı komut girdiniz sıranızı kaybettiniz!")
        if(y.can<=0):
            break
        print(p2,"adlı kullanıcının sırası:")
        giris2 = int(input())
        if (giris2 == 1):
            x.saldiriugra(y.saldir())
        elif (giris2 == 2):
            y.canbas()
        elif (giris2 == 3):
            y.gucartir()
        else:
            print("Hatalı komut girdiniz sıranızı kaybettiniz!")
    break

if(x.can<=0):
    print("\n\n",p2," adlı kullanıcı oyunu kazandı!")
else:
    print("\n\n",p1," adlı kullanıcı oyunu kazandı")

print("\n---Hasar Tablosu---")
i=0
while i<=((len(oyunsinif.gunluk))-1):
    print(oyunsinif.gunluk[i],":",oyunsinif.gunluk[i+1])
    i += 2