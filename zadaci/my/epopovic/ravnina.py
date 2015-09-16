#snimit ce celiju

from math import sqrt

class Tocka:
    '''Opis klase
    2D tocke u ravnini
    '''
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def norm(self):
        return sqrt(self.x**2+self.y**2)
    def __repr__(self):
        return "Tocka x={0}, y={1}".format(self.x,self.y)

    
class Vektor(Tocka):
    '''
    Nasljedjuje klasu tocka
    '''
    def __add__(self,b):
        return Vektor(x=self.x+b.x,y=self.y+b.y)
    def __sub__(self,b):
        return Vektor(x=self.x-b.x,y=self.y-b.y)

    def __mul__(self, b):
        if type(b) == type(self):
            return self.x*b.x+self.y*b.y
        elif type(b) == type(1) or type(b) == type(1.0):
            return Vektor(x=self.x*b, y=self.y*b)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return "Vektor x={0}, y={1}".format(self.x,self.y)