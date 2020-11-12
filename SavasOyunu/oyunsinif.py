import random
gunluk=[]
class Player:
    can=200
    saldirigucu=5

    def __init__(self,name):
        self.isim=name

    def saldiriugra(self,dmg):
        self.can-=dmg
        print(self.isim,":",self.can," canım kaldı!")

    def saldir(self):
        self.hasar=random.randint(0,10)*self.saldirigucu
        print(self.isim,": Rakibe",self.hasar," hasar vuruldu!")
        gunluk.append(self.isim)
        gunluk.append(self.hasar)
        return self.hasar

    def gucartir(self):
        self.plusguc=random.randint(0,3)
        self.saldirigucu+=self.plusguc
        print(self.isim,": Saldırı gücüm",self.plusguc," arttı.Artık",self.saldirigucu,"saldırı gücüm var.")


    def canbas(self):
        self.pluscan=random.randint(15,30)
        self.can+=self.pluscan
        print(self.isim,": Canım ",self.pluscan," kadar arttı.Artık",self.can," canım var")
