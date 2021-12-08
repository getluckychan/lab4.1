from main import Matrix2x2, ComplexNumbers, VectorWith10Elements


def main():
    number_result = ComplexNumbers(1) + ComplexNumbers(2)
    vector_result = VectorWith10Elements(1234567890) + VectorWith10Elements(1987654321)
    matrix_result = Matrix2x2(([1, 2], [3, 4])) + Matrix2x2(([4, 3], [2, 1]))
    pointer_list = [number_result, vector_result, matrix_result]
    pointers = [id(pointer_list[0]), id(pointer_list[1]), id(pointer_list[2])]
    return pointers, type(number_result), type(matrix_result), type(matrix_result)


print(main())
