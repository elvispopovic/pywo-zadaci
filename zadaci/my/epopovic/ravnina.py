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