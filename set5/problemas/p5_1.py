class Formiga:
    path = "NESO"
    coords = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "O": (0, -1)
    }

    def __init__(self, grid_size):
        self.dir = "N"  # a formiga começa virada para frente (norte)
        # a formiga começa no centro do grid
        self.position = grid_size // 2, grid_size // 2
        self.grid_size = grid_size  # esse é o tamanho do grid atual que a formiga está

    def get_dir(self):
        return self.dir

    def get_pos(self):
        return self.position

    def get_move(self):
        return Formiga.coords[self.get_dir()]

    def is_in_grid(self):
        # verificar se a formiga está dentro do grid
        if self.grid_size > self.position[0] >= 0 and self.grid_size > self.position[1] >= 0:
            return True

        return False

    def new_dir(self, move):
        index = Formiga.path.find(self.get_dir())

        if move == "R": new_index = (index + 1) % 4
        elif move == "L": new_index = (index - 1) % 4
            
        self.dir = Formiga.path[new_index]

    def update_pos(self, move):
        new_x = self.get_pos()[0] + move[0]
        new_y = self.get_pos()[1] + move[1]

        self.position = new_x, new_y

    def move(self, grid):
        position = self.get_pos()  # posição atual

        grid.update_cell(position)  # alterar o grid com a posição atual

        # mudar a posição de acordo com o próximo movimento
        self.update_pos(self.get_move())

        try:
            self.new_dir(grid.get_rule(self.get_pos()))  # girar formiga
        except:
            pass  # não encontrei outro jeito de burlar o erro, já que queremos saber quando a formiga sai/estoura o grid


class Grid:
    def __init__(self, size, rules):
        # criando o grid inicial: todos os espaço começam zerados
        self.grid = []

        for i in range(size):
            grid_temp = []
            self.grid.append(grid_temp)
            for j in range(size):
                grid_temp.append(0)

        # precisamos saber o número de cores máximos de acordo com o comprimento de nossa str `rules`
        self.color_length = len(rules)
        self.rules = rules

    def get_grid(self):
        # retorna o grid como uma lista de listas
        return self.grid

    def get_color(self, position):
        # retorna a "cor" de uma célula em uma dada posição (x,y)
        return self.grid[position[0]][position[1]]

    def get_rule(self, position):
        # encontrar a regra "R" ou "L" do momento atual
        color = self.get_color(position)
        return self.rules[color]

    def update_cell(self, position):
        # incrementar o valor/"cor" da célula
        x, y = position

        self.grid[x][y] = (self.grid[x][y] + 1) % self.color_length


def run_langton(rules, size):
    form = Formiga(size)
    grid = Grid(size, rules)
    counter = 0

    while form.is_in_grid():
        form.move(grid)
        counter += 1

    return (counter, grid.get_grid(), counter)

print(run_langton("RLRR", 51))