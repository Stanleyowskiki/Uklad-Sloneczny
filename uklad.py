from wektory import Wektor
import matplotlib.pyplot as plt
Gg = 6.6743*10**(-11) #N*m^2/kg^2
dt = 120000
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
    def __init__(self, nazwa,solar_system, masa,pozycja=(0, 0, 0),predkosc=(0, 0, 0)):
        self.nazwa = nazwa
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
        wartoscsily = (Gg * self.masa * other.masa) / (dlugoscr ** 2)
        sila = promien.wersor() * wartoscsily

        odwroc = 1
        for obiekt in self, other:
            przysp = sila/(obiekt.masa)
            obiekt.predkosc += przysp * dt * odwroc
            odwroc *= -1
                
Uklad_Sloneczny = Uklad(0)
#dla wszystkich planet biorę peryhelium (w metrach) https://nssdc.gsfc.nasa.gov/planetary/factsheet/planet_table_ratio.html
slonce = Obiekt(nazwa="Slonce",solar_system=Uklad_Sloneczny ,masa=1.989*10**(30), pozycja=(0,0,0), predkosc=(0,0,0))
merkury = Obiekt(nazwa="Merkury",solar_system=Uklad_Sloneczny ,masa=3.3011*10**(23), pozycja=(46000000000,0,0), predkosc=(0,58980,0))
wenus = Obiekt(nazwa="Wenus",solar_system=Uklad_Sloneczny ,masa=4.867*10**(24), pozycja=(107476002000,0,0), predkosc=(0,35260,0))
ziemia = Obiekt(nazwa="Ziemia",solar_system=Uklad_Sloneczny ,masa=5.97*10**(24), pozycja=(147100000000,0,0), predkosc=(0,30300,0))
mars = Obiekt(nazwa="Mars",solar_system=Uklad_Sloneczny ,masa=0.64169*10**(24), pozycja=(206650000000,0,0), predkosc=(0,26500,0))
jowisz = Obiekt(nazwa="Jowisz",solar_system=Uklad_Sloneczny ,masa=1.898*10**(27), pozycja=(740595000000,0,0), predkosc=(0,13720,0))
saturn = Obiekt(nazwa="Saturn",solar_system=Uklad_Sloneczny ,masa=568.32*10**(24), pozycja=(1357554000000,0,0), predkosc=(0,10180,0))
uran = Obiekt(nazwa="Uran",solar_system=Uklad_Sloneczny ,masa=86.811*10**(24), pozycja=(2732696000000,0,0), predkosc=(0,7110,0))
neptun = Obiekt(nazwa="Neptun",solar_system=Uklad_Sloneczny ,masa=102.409*10**(24), pozycja=(4471050000000,0,0), predkosc=(0,5500,0))

print(f'Ilość obiektów w układzie: {Uklad_Sloneczny.iloscObiektow}')


while t < 50000000:
    Uklad_Sloneczny.oblicz_wszystkie_sily()
    Uklad_Sloneczny.rusz_uklad()
    #for obiekty in Uklad_Sloneczny.tablicaObiektow:
        #print(f'{obiekty.nazwa}: {obiekty.pozycja}')
        #plt.scatter(obiekty.pozycja[0], obiekty.pozycja[1], s=5)
    plt.scatter(slonce.pozycja[0], slonce.pozycja[1], s=1, color="orange")
    plt.scatter(wenus.pozycja[0], wenus.pozycja[1], s=1, color="blue")
    plt.scatter(ziemia.pozycja[0], ziemia.pozycja[1], s=1, color="green")
    # plt.scatter(mars.pozycja[0], mars.pozycja[1], s=1, color="#88c999")
    # plt.scatter(jowisz.pozycja[0], jowisz.pozycja[1], s=1, color='red')
    # plt.scatter(saturn.pozycja[0], saturn.pozycja[1], s=1, color='black')
    # plt.scatter(uran.pozycja[0], uran.pozycja[1], s=1, color='yellow')
    #plt.scatter(neptun.pozycja[0], neptun.pozycja[1], s=1, color='pink')
    t += dt

plt.title("Solar System", fontsize=19)
plt.show()
