import random


class Matrix(object):
    '''
    Class that defines the matrix structure and some methods to interact with them.
    '''

    def __init__(self, size, define_it=False):
        self.size = size
        self.matrix = None
        self.create_matrix_manually() if define_it else self.generate_matrix()

    def __str__(self):
        matrix_string = ''
        for row in self.matrix:
            for element in row:
                matrix_string += str(element) + ' | '
            matrix_string = matrix_string[:-3] + \
                '\n' + ('- - ' * self.size)[:-2] + '\n'
        return ('- - ' * self.size)[:-2] + '\n' + matrix_string

    def generate_matrix(self):
        self.matrix = [[random.randint(1, 4) for j in range(
            self.size)] for i in range(self.size)]

    def create_matrix_manually(self):
        pass

    def min_algorithm(self):
        pass

    def max_algorithm(self):
        pass


if __name__ == '__main__':
    matrix_size = int(input('Ingrese el tamaño de la matriz: '))
    matrix = Matrix(matrix_size)
    print(matrix)
