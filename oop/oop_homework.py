
import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return self.height * math.pi * (self.radius) ** 2

    def surface_area(self):
        top = math.pi * (self.radius ** 2)

        return (2 * top) + (2* math.pi * self.radius * self.height)

my_cylinder = Cylinder(2,3)
print(my_cylinder.volume())
print(my_cylinder.surface_area())

