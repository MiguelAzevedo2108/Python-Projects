import math

class Line:

    def __init__(self,coord1,coord2):
        self.coord1 = coord1
        self.coord2 = coord2
        pass

    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coord1
        x2, y2 = self.coord2

        return (y2-y1)/(x2-x1)

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        pass

    def volume(self):
        return self.height * math.pi *self.radius **2

    def surface_area(self):
        return (2*math.pi*self.height*self.radius) + (2*math.pi*self.radius**2)


c1 = (3,2)
c2 = (8,10)

line = Line(c1,c2)
cylinder = Cylinder(2,3)


if __name__ == '__main__':
    print("Running")
    print(line.slope())
    print(cylinder.surface_area())





