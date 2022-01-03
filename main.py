lista_planet = []
from time import sleep

class Cialo_niebieskie:
    def __init__(self, Masa, pozycja, predkosc, przyspieszenie_w):
        self.Masa = Masa
        self.pozycja = pozycja
        self.predkosc = predkosc
        self.przysp_w = przyspieszenie_w
        lista_planet.append(self)

    def ruch(self, tik):
        for i in range(3):
            self.pozycja[i] += self.predkosc[i] * tik
            self.predkosc[i] += self.przysp_w[i] * tik

Pila = Cialo_niebieskie(1,[0,0,0],[10,5,3],[0,0,0])
while True:
    Pila.ruch(1)
    sleep(1)
    print(Pila.pozycja)