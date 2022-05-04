class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, mat)) for mat in self.input])

    def __add__(self, other):
        total = ''
        if len(self.input) == len(other.input):
            for mat_1, mat_2 in zip(self.input, other.input):
                if len(mat_1) != len(mat_2):
                    return

                mat_summ = [x + y for x, y in zip(mat_1, mat_2)]
                total += ' '.join(map(str, mat_summ)) + '\n'
        else:
            return
        return total


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86], [35, 32]])
matrix_2 = Matrix([[-1, -8], [-7, 9], [5, 81], [-12, 1]])
print(matrix_1)
print("----------")
print(matrix_1 + matrix_2)