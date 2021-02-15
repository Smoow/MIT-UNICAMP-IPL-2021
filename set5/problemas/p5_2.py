class Matrix:
    def __init__(self, list_line):
        self.matrix = list_line

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def get(self, r, c):
        return self.matrix[r][c]

    def set(self, r, c, val):
        self.matrix[r][c] = val
        return

    def row(self, n):
        return self.matrix[n]

    def col(self, n):
        elements = []
        for row in self.matrix:
            for index, el in enumerate(row):
                if index == n:
                    elements.append(el)

        return elements

    def transpose(self):
        trans_matrix = []
        for i in range(self.size()[1]):
            trans_matrix.append(self.col(i))

        return Matrix(trans_matrix)

    def add(self, other):
        # construindo a matriz adequada preenchida com zeros
        result = [[0 for i in range(self.size()[1])]
                  for j in range(self.size()[0])]

        # para instâncias floats ou ints
        if isinstance(other, (int, float)):
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    result[i][j] = self.get(i, j) + other

            return Matrix(result)

        # para instâncias Matrix com dimensões apropriadas
        if isinstance(other, Matrix) and other.size() == self.size():
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    result[i][j] = self.get(i, j) + other.get(i, j)

            return Matrix(result)

        return None

    def sub(self, other):
        # construindo a matriz adequada preenchida com zeros
        result = [[0 for i in range(self.size()[1])]
                  for j in range(self.size()[0])]

        # para instâncias floats ou ints
        if isinstance(other, (int, float)):
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    result[i][j] = self.get(i, j) - other

            return Matrix(result)

        # para instâncias Matrix com dimensões apropriadas
        if isinstance(other, Matrix) and other.size() == self.size():
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    result[i][j] = self.get(i, j) - other.get(i, j)

            return Matrix(result)

        return None

    def mul(self, other):
        # construindo a matriz adequada preenchida com zeros
        result = [[0 for i in range(self.size()[1])]
                  for j in range(self.size()[0])]

        # para instâncias floats ou ints
        if isinstance(other, (int, float)):
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    result[i][j] = self.get(i, j) * other

            return Matrix(result)

        # para instâncias Matrix com dimensões apropriadas
        if isinstance(other, Matrix) and other.size()[0] == self.size()[1]:
            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    self_row = self.row(i)
                    other_col = other.col(j)

                    value_total = 0
                    for el_self, el_other in zip(self_row, other_col):
                        value_total += el_self * el_other

                    result[i][j] = value_total

            return Matrix(result)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)
