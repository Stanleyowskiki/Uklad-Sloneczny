from wektory import wektor
G=5
dt=1000
t=0

class Obiekt:
    def __init__(
        self,
        masa,
        pozycja=(0,0,0),
        predkosc=(0,0,0),
    ):
        self.masa = masa
        self.pozycja = pozycja
        self.predkosc = wektor(*predkosc)
    
    def nowa_pozycja(self,other):
        promien=wektor(*other.pozycja)-wektor(*self.pozycja)
        dlugosc_r=promien.dlugosc_w

        wartosc_sily=G*self.masa*other.masa/(dlugosc_r*dlugosc_r)
        sila=promien.wersor*wartosc_sily
        a=sila/self.masa
        self.predkosc+=a*dt
        self.pozycja+=self.predkosc*dt

slonce= Obiekt(masa=2*(10**30),pozycja=(0,0,0),predkosc=(0,0,0))
ziemia= Obiekt(masa=6*(10**24),pozycja=(147100000000,0,0),predkosc=(0,30300,0))

while t<(10**7):
    ziemia.nowa_pozycja(slonce)
    print(ziemia.pozycja)
    t+=dt
