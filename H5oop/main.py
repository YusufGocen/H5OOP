class hesap:
    def __init__(self,say1,say2):
        self.say1=say1
        self.say2=say2

    def carp(self):
        sonuc=self.say1*self.say2
        return sonuc

    def bol(self):
        sonuc=self.say1/self.say2
        return sonuc

    def topla(self):
        sonuc=self.say1+self.say2
        return sonuc

    def cikar(self):
        sonuc=self.say1-self.say2
        return sonuc

    def yazdır(self):
        toplam=self.topla()
        print('sayıların toplamı:',toplam)
        carpma=self.carp()
        print('sayiların çarpımı:',carpma)
        bolme=self.bol()
        print('sayıların bölümü:',bolme)
        cikart=self.cikar()
        print('sayıların farkı:',cikart)

        obje=hesap(5,3)
        A=obje.carp()