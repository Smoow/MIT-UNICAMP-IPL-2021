class Ant:
    DIRS = "NESW"
    MOVES = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    def __init__(self, grid_size):
        self.angle = "N"  # direção da formiga
        self.pos = grid_size // 2, grid_size // 2  # posição da formiga
        self.grid_size = grid_size  # tamanho do grid em que a formiga está

    def get_pos(self):
        """retorna posição da formiga como tupla (x, y)"""
        return self.pos

    def get_angle(self):
        """retorna direção ("N","S","E","W")"""
        return self.angle

    def get_move(self):
        """determina movimento de acordo com direção; tupla (dx,dy)"""
        return Ant.MOVES[self.get_angle()]

    def in_grid(self):
        """checa se formiga está dentro do grid ainda
        checa se alguma coordenada está além do permitido para o grid"""
        return 0 <= self.pos[0] < self.grid_size and 0 <= self.pos[1] < self.grid_size

    def set_new_dir(self, instr):
        """define uma nova direção (gira de acordo com cor da nova célula)"""
        cur_index = Ant.DIRS.find(self.get_angle())  # índice atual na string Ant.DIRS

        if instr == "R":
            new_index = (cur_index + 1) % 4  # wrap around, move uma pra frente
        elif instr == "L":
            new_index = (cur_index - 1) % 4  # wrap around, move uma pra trás

        self.angle = Ant.DIRS[new_index]  # usa novo índice para determinar nova direção

    def set_new_pos(self, move):
        """atualiza posição da formiga de acordo com um movimento (dx,dy)
        mudando de posição (x,y) para (x+dx,y+dy)"""
        new_x = self.get_pos()[0] + move[0]
        new_y = self.get_pos()[1] + move[1]

        self.pos = new_x, new_y

    def move(self, grid):
        """contém o movimento completo de andar: incrementa cor da posição atual,
        avança uma célula, e determina nova orientação"""
        position = self.get_pos()  # posição atual da formiga

        grid.update_cell(position)  # muda a cor da célula em que está

        self.set_new_pos(self.get_move())  # andamos na direção correta

        try:
            self.set_new_dir(grid.get_dir_rule(self.get_pos()))  # giramos a formiga
        except IndexError:
            pass  # nesse caso a formiga saiu do grid, o que será percebido por in_grid em sequência

class Grid:
    def __init__(self, size, rules, init_val=0):
        # cria uma lista de listas de tamanho size x size com init_val em todas as posições
        self.grid = [[init_val for _ in range(size)][:] for _ in range(size)]
        # número de cores dado pelo comprimento da string de regras
        self.color_range = len(rules)
        self.rules = rules

    def get_grid(self):
        """retorna o grid como lista de listas"""
        return self.grid

    def get_cell_color(self, pos):
        """retorna cor de uma célula específica em (x,y), dado por pos"""
        return self.grid[pos[0]][pos[1]]

    def update_cell(self, pos, inc=1):
        """incrementa o valor da célula em pos por inc (padrão é 1)"""
        x, y = pos
        # módulo é usado para dar a volta depois do último número
        self.grid[x][y] = (self.grid[x][y] + inc) % self.color_range

    def get_dir_rule(self, pos):
        """retorna a regra ("R" ou "L") encontrada em pos de acordo com cor atual"""
        color = self.get_cell_color(pos)
        return self.rules[color]


def run_langton(rules, size):
    """
    Simula o movimento da formiga de Langton como descrito no problema até que ela
    sai do grid.

    Args:
        rules: string de regras (e.g. "RLRLR")
        size: tamanho do lado do grid quadrado (grid tem tamanho size x size)

    Returns:
        tupla (count, grid_list): count é o número de passos até sair do grid
            (contando o último) e grid_list é uma lista aninhada contendo as cores
            para cada posição do grid depois do movimento da formiga
    """
    ant = Ant(size)  # cria a formiga
    grid = Grid(size, rules)  # cria o grid em que a formiga irá andar
    count = 0

    while ant.in_grid():  # enquanto a formiga não sair do grid
        ant.move(grid)  # próximo movimento
        count += 1  # mais um passo na conta!

    return count, grid.get_grid()
