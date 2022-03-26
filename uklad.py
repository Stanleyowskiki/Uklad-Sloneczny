from wektory import Wektor
G = 6.6743*10**(-11) #N*m^2/kg^2
dt = 1000
t = 0

class Uklad:
    def __init__(self, iloscObiektow):
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
    def __init__(self, solar_system, masa,pozycja=(0, 0, 0),predkosc=(0, 0, 0)):
        self.solar_system = solar_system
        self.masa = masa
        self.pozycja = pozycja
        self.predkosc = Wektor(*predkosc)
        self.solar_system.dodajObiekt(self)
        
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
        
        # a_self = sila / self.masa
        # self.predkosc += dt * a_self
        # a_other = sila / other.masa
        # other.predkosc -= dt * a_other
        odwroc = 1
        for obiekt in self, other:
            przysp = sila/ obiekt.masa
            obiekt.predkosc += przysp * dt * odwroc
                
Uklad_Sloneczny = Uklad(0)
slonce = Obiekt(solar_system=Uklad_Sloneczny ,masa=1.989*10**(30), pozycja=(0,0,0), predkosc=(0,0,0))
ziemia = Obiekt(solar_system=Uklad_Sloneczny ,masa=5.97*10**(24), pozycja=(147100000000,0,0), predkosc=(0,30300,0)) #dla wszystkich planet biorę peryhelium (w metrach)
wenus = Obiekt(solar_system=Uklad_Sloneczny ,masa=4.867*10**(24), pozycja=(107476002000,0,0), predkosc=(0,99,0))

print(Uklad_Sloneczny.iloscObiektow)
