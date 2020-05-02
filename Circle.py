import math
import numpy as np
class Circle:
    def __init__(self,radius=1.0):
        self.radius=radius
    def __str__(self):
        return f'This is a circle with radius {self.radius:.2f}'
    def getarea(self):
        return self.radius*self.radius*np.pi
    def __repr__(self):
        return f'Circle(radius={self.radius})'

c=Circle(2)
print(repr(c))




