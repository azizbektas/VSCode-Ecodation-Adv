'''from abc import ABC, abstractmethod
class Ciz(ABC):
    @abstractmethod
    def cizAksiyonu(self):
        pass

class Kare(Ciz):
    def cizAksiyonu(self):
        print("kare çizmek için gerekli parametreler geldi, aksiyonu çiz sınıfından çağıcacağım")
        return super().cizAksiyonu()

# ciz = Ciz()
# ciz.cizAksiyonu() # :-(
kareNesnesi = Kare()
kareNesnesi.cizAksiyonu()'''









from abc import ABC, abstractmethod
import turtle

class Ciz(ABC):
    def __init__(self, adim1, adim2, derece) -> None:
        self.adim1= adim1
        self.adim2= adim2
        self.derece= derece

    @abstractmethod
    def cizAksiyonu(self):
        import random as rnd
        t = turtle.Turtle()
        t.pensize(3)
        colors=["green", "red", "black"]   
        x= 100
        y = 100 
 
        for i in range(5):
            t.penup()  
            t.goto(x, x)   
            t.pendown() 
            for i in range(2):                
                t.color(rnd.choice(colors))
                t.forward(self.adim1)
                t.left(self.derece)
                t.forward(self.adim2)
                t.left(self.derece)
            x -= 10
            y -= 10
        input("devam etmek için, enter...")

class Kare(Ciz):
    def __init__(self, adim1, adim2, derece) -> None:
        super().__init__(adim1, adim2, derece)

    def cizAksiyonu(self): 
        super().cizAksiyonu()

class Dikdortgen(Ciz):
    def __init__(self, adim1, adim2, derece) -> None:
        super().__init__(adim1, adim2, derece)

    def cizAksiyonu(self):
        super().cizAksiyonu()


# kareNesnesi= Kare(100, 100, 90)
# kareNesnesi.cizAksiyonu()
dikdortgenNesnesi=Dikdortgen(200, 100, 90)
dikdortgenNesnesi.cizAksiyonu()