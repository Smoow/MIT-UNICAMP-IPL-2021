class Matrix:
    def __init__(self, input_list):
        self.mat = input_list

    def size(self):
        return len(self.mat), len(self.mat[0])

    def get(self, r, c):
        return self.mat[r][c]

    def set(self, r, c, val):
        self.mat[r][c] = val

    def row(self, n):
        return self.mat[n]

    def col(self, n):
        out = []

        for row in self.mat:
            for ind, elem in enumerate(row):
                if ind == n:  # pegamos o elemento com índice n em cada linha (lista aninhada)
                    out.append(elem)

        return out

    def transpose(self):
        cols = [self.col(i) for i in range(self.size()[1])]  # lista de colunas

        return Matrix(cols)

    def add(self, other):
        # forma matriz "vazia" (preenchida com None's) de formato apropriado
        out = [[None for _ in range(self.size()[1])][:] for _ in range(self.size()[0])]

        if isinstance(other, Matrix) and other.size() == self.size():  # mesmo formato exatamente
            for r in range(self.size()[0]):
                for c in range(self.size()[1]):
                    # adicionamos elementos análogos
                    out[r][c] = self.get(r, c) + other.get(r, c)

            return Matrix(out)

        if isinstance(other, (int, float)):
            for r in range(self.size()[0]):
                for c in range(self.size()[1]):
                    # adicionamos o mesmo valor para todas as entradas
                    out[r][c] = self.get(r, c) + other

            return Matrix(out)

        return None

    def sub(self, other):
        # forma matriz "vazia" (preenchida com None's) de formato apropriado
        out = [[None for _ in range(self.size()[1])][:] for _ in range(self.size()[0])]

        if isinstance(other, Matrix) and other.size() == self.size():  # mesmo formato exatamente
            for r in range(self.size()[0]):
                for c in range(self.size()[1]):
                    # subtraímos elementos análogos
                    out[r][c] = self.get(r, c) - other.get(r, c)

            return Matrix(out)

        if isinstance(other, (int, float)):
            for r in range(self.size()[0]):
                for c in range(self.size()[1]):
                    # subtraímos o mesmo valor para todas as entradas
                    out[r][c] = self.get(r, c) - other

            return Matrix(out)

        return None

    def mul(self, other):
        if isinstance(other, (int, float)):
            # forma matriz "vazia" (preenchida com None's) de formato apropriado
            out = [[None for _ in range(self.size()[1])][:] for _ in range(self.size()[0])]
            for r in range(self.size()[0]):
                for c in range(self.size()[1]):
                    # multiplicamos todas as entradas pelo mesmo valor
                    out[r][c] = self.get(r, c) * other

            return Matrix(out)

        if isinstance(other, Matrix) and other.size()[0] == self.size()[1]:  # colunas do primeiro = linhas do segundo
            # forma matriz "vazia" (preenchida com None's) de formato apropriado
            out = [[None for _ in range(other.size()[1])][:] for _ in range(self.size()[0])]
            for r in range(self.size()[0]):
                for c in range(other.size()[1]):
                    self_row = self.row(r)
                    other_col = other.col(c)

                    total = 0
                    for el_self, el_other in zip(self_row, other_col):
                        # somamos todos os produtos dos elementos das linhas e colunas correspondentes
                        total += el_self * el_other

                    out[r][c] = total

            return Matrix(out)
        
        return None

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)
