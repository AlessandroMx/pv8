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
        self.matrix = [[random.randint(0, 4) for j in range(
            self.size)] for i in range(self.size)]

    def create_matrix_manually(self):
        pass

    def min_algorithm(self, numbers):
        min_num = None
        min_counter = 0
        for key, value in numbers.items():
            min_num = key if min_num == None or value > min_counter and key < min_num else min_num
        return min_num

    def max_algorithm(self, numbers):
        max_num = None
        max_counter = 0
        for key, value in numbers.items():
            max_num = key if max_num == None or value > max_counter and key > max_num else max_num
        return max_num

    def travel_neighbors(self, x, y):
        numbers = {}
        for i in range(3):
            for j in range(3):
                x_pos = x + i - 1
                y_pos = y + j - 1
                if x_pos >= 0 and y_pos >= 0 and x_pos < self.size and y_pos < self.size:
                    tmp_num = self.matrix[x_pos][y_pos]
                    if not tmp_num in numbers:
                        numbers.update({tmp_num: 1})
                    else:
                        numbers[tmp_num] += 1
        return numbers

    def travel_matrix(self):
        '''
        Method for visiting each matrix cell and apply the needed algorithms.
        '''
        min_algorithm_matrix = []
        max_algorithm_matrix = []
        for x in range(self.size):
            tmp_min_row = []
            tmp_max_row = []
            for y in range(self.size):
                numbers = self.travel_neighbors(x, y)
                tmp_min_row.append(self.min_algorithm(numbers))
                tmp_max_row.append(self.max_algorithm(numbers))
            min_algorithm_matrix.append(tmp_min_row)
            max_algorithm_matrix.append(tmp_max_row)
        print(min_algorithm_matrix)
        print(max_algorithm_matrix)


if __name__ == '__main__':
    matrix_size = int(input('Ingrese el tamaño de la matriz: '))
    matrix = Matrix(matrix_size)
    print(matrix)
    matrix.travel_matrix()
