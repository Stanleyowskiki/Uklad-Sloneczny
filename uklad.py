from wektory import Wektor
G = 5.0
dt = 1000
t = 0

class Uklad:
    def _init_(self, iloscObiektow):
        self.iloscObiektow = iloscObiektow
        self.tablicaObiektow = []
        
    def dodajObiekt(self, obiekt):
        self.tablicaObiektow.append(obiekt)
        self.iloscObiektow += 1
        
    def rusz_uklad(self):
        self.tablicaObiektow.sort(key=lambda item: item.pozycja[0])
        for obiekt in self.tablicaObiektow:
            obiekt.rusz()
        
    def oblicz_wszystkie_sily(self):
        kopia = self.tablicaObiektow.copy()
        for idx, first in enumerate(kopia):
            for second in kopia[idx + 1:]:
                first.przys_grawitacyjne(second)
                
                
class  Obiekt:
    def __init__(self, uklad_sl, masa,pozycja=(0, 0, 0),predkosc=(0, 0, 0)):
        self.uklad_sl = uklad_sl
        self.masa = masa
        self.pozycja = pozycja
        self.predkosc = Wektor(*predkosc)
        self.uklad_sl.dodajObiekt(self)
        
    def rusz(self):
        self.pozycja = (
            self.pozycja[0] + dt*self.predkosc[0],
            self.pozycja[1] + dt*self.predkosc[1],
            self.pozycja[2] + dt*self.predkosc[2],
        )
    
    def przys_grawitacyjne(self, other):
        promien = Wektor(*other.pozycja) - Wektor(*self.pozycja)
        dlugoscr = promien.dlugosc_w()
        wartoscsily = (G * self.masa * other.masa) / (dlugoscr ** 2)
        sila = promien.wersor() * wartoscsily
        
        a_self = sila / self.masa
        self.predkosc += dt * a_self
        a_other = sila / other.masa
        other.predkosc -= dt * a_other
                
Uklad_Sloneczny = Uklad()
slonce = Obiekt(uklad_sl=Uklad_Sloneczny ,masa=5, pozycja=(0,0,0), predkosc=(0,0,0))
ziemia = Obiekt(uklad_sl=Uklad_Sloneczny ,masa=1, pozycja=(200,0,0), predkosc=(0,70,0))
wenus = Obiekt(uklad_sl=Uklad_Sloneczny ,masa=3, pozycja=(100,0,0), predkosc=(0,99,0))

print(Uklad_Sloneczny.iloscObiektow)
