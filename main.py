from abc import ABC, abstractmethod
from numpy import array, sum, matrix
import ctypes


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


number_first = ComplexNumbers(1)
number_second = ComplexNumbers(2)
vector_first = VectorWith10Elements(1234567890)
vector_second = VectorWith10Elements(1987654321)
matrix_first = Matrix2x2(([1, 2], [3, 4]))
matrix_second = Matrix2x2(([4, 3], [2, 1]))
number_result = number_first + number_second
vector_result = vector_first + vector_second
matrix_result = matrix_first + matrix_second
pointer_list = [number_result, vector_result, matrix_result]
first_pointer = id(pointer_list[0])
second_pointer = id(pointer_list[1])
third_pointer = id(pointer_list[2])
pointers = [first_pointer, second_pointer, third_pointer]
print(type(number_result))
print(type(matrix_result))
print(type(matrix_result))
print(pointers)