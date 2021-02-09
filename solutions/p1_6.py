p_d = 101

cells_in = 0
cells_total = 0

# encontra todos os pares de coordenadas do grid
for x in range(- (p_d // 2), p_d // 2 + 1):
    for y in range(- (p_d // 2), p_d // 2 + 1):
        cells_total += 1  # mais uma célula do total

        dist = (x ** 2 + y ** 2) ** 0.5  # distância do centro
        if dist <= p_d / 2:
            cells_in += 1  # dentro do círculo se menor que p_d / 2

out = 4 * cells_in / cells_total  # estimativa de pi
