class Bank:

    hesaptakipara=3000
    def paracek(self,miktar):
        self.miktar=miktar
        if(self.miktar>self.hesaptakipara):
            print("Yetersiz bakiye!")
        else:
            print("Hesabınızdan",self.miktar,"TL çekildi...")
            self.hesaptakipara=self.hesaptakipara-self.miktar
    def parayatir(self,miktar):
        self.miktar=miktar
        print("Hesabınıza",self.miktar,"TL yatırıldı...")
        self.hesaptakipara=self.hesaptakipara+self.miktar
    def kontrol(self):
        print("Hesabınızda",self.hesaptakipara,"TL var.")

