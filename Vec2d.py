import math

class Vec2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def display(self):
        return {f'{self.x} {self.y}'} 

    def __add__(self,other):
        return Vec2d(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vec2d(self.x-other.x,self.y-other.y)
    def length(self):  
        return math.sqrt( self.x**2 + self.y**2 )
    def distance(self,other):
        return (other-self).length()
    def  __str__(self):   
        return (f'Vec2d({self.x},{self.y}')



