"""Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method."""


from math import sqrt


class CustomError(Exception):
    def __init__(self, message = "Vectors have different length !"):
        self.message = message
        super().__init__(self.message)


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def add(self, other_vector):
        if len(self.vector) != len(other_vector.vector):
            raise CustomError
        return Vector([self.vector[i] + other_vector.vector[i] for i in range(len(self.vector))])

    def subtract(self, other_vector):
        if len(self.vector) != len(other_vector.vector):
            raise CustomError
        return Vector([self.vector[i] - other_vector.vector[i] for i in range(len(self.vector))])

    def dot(self, other_vector):
        if len(self.vector) != len(other_vector.vector):
            raise CustomError
        return sum(self.vector[i] * other_vector.vector[i] for i in range(len(self.vector)))

    def norm(self):
        return sqrt(sum(i**2 for i in self.vector))

    def equals(self, other_vector):
        return self.vector == other_vector.vector

    def __str__(self):
        a = "("
        b = ")"
        result = ",".join(str(i) for i in self.vector)
        return a + result + b


