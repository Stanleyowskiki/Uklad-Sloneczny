import math

class wektor:
    def __init__(self, x=0, y=0, z=0):  #c++-konstr domyslny
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    def __getitem__(self, item):  #wprowadzenie wektora (C++-konstr glowny)
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("Wektor powinien zawierac tylko trzy elementy")

    def __add__(self, other):  #przeciazenie operatora dodawania
        return wektor(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,)
    
    def __sub__(self, other):  #przeciazenie operatora odejmowania
        return wektor(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,)

    def __mul__(self, other):  #przeciazenie operatora mnozenia
        if isinstance(other, wektor):  #iloczyn skalarny
            return (
                    self.x * other.x
                    + self.y * other.y
                    + self.z * other.z)
        elif isinstance(other, (int, float)):  #mnozenie przez liczbe
            return wektor(
                self.x * other,
                self.y * other,
                self.z * other,)

    def __truediv__(self, other): #przeciaenie operatora dzielenia (przez liczbe)
        if isinstance(other, (int, float)):
            return wektor(
                self.x / other,
                self.y / other,
                self.z / other,)

    def dlugosc_w(self):   #obliczanie dlugosci wektora
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def wersor(self):
        dlugosc = self.dlugosc_w()
        return wektor(
            self.x / dlugosc,
            self.y / dlugosc,
            self.z / dlugosc,
        )
