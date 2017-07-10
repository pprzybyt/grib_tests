class Vect3D:

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # String represntation

    def __str__(self):
        return ("<%s, %s, %s>" % (self.x, self.y, self.z))

    # Produce a copy of itself
    def __copy__(self):
        return Vect3D(self.x, self.y, self.z)

    # Signing
    def __neg__(self):
        return Vect3D(-self.x, -self.y, -self.z)

    # Scalar Multiplication
    def __mul__(self, number):
        return Vect3D(self.x * number, self.y * number, self.z * number)

    def __rmul__(self, number):
        return self.__mul__(number)

    # Division
    def __div__(self, number):
        return self.__copy__() * (number**-1)

    # Arithmetic Operations
    def __add__(self, operand):
        return Vect3D(self.x + operand.x, self.y + operand.y, self.z + operand.z)

    def __sub__(self, operand):
        return self.__copy__() + -operand

    # Operations

    def normalize(self):
        return self.__div__(self.magnitude())

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (.5)

    # cross product
    def cross(self, operand):
        return Vect3D(self.y * operand.z - self.z * operand.y,
                      self.z * operand.x - self.x * operand.z,
                      self.x * operand.y - self.y * operand.x)
