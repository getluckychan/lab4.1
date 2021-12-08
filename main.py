from abc import ABC, abstractmethod
from numpy import array, sum, matrix


class Add(ABC):

    @abstractmethod
    def __add__(self, other):
        pass


class ComplexNumbers(Add):
    def __init__(self, number):
        self.number = complex(number)

    def __add__(self, other):
        return self.number + other.number


class VectorWith10Elements(Add):
    def __init__(self, vector):
        self.vector = array([int(x) for x in str(vector)])

    def __add__(self, other):
        return sum([self.vector, other.vector])


class Matrix2x2(Add):
    def __init__(self, for_matrix):
        self.matrix = matrix(for_matrix)

    def __add__(self, other):
        return self.matrix.sum(dtype='float')
