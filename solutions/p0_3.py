kwh_used = 1000

if kwh_used <= 500:
    # Todos os iniciais custam 0.45
    out = kwh_used * 0.45
elif kwh_used <= 1500:
    # Usamos todos os 500 disponíveis a 0.45, e o resto é mais caro a 0.74
    out = 500 * 0.45 + (kwh_used - 500) * 0.74
elif kwh_used <= 2500:
    # Mesma lógica para o resto: calcula o custo das faixas anteriores e
    # adiciona a diferença da nova faixa
    out = 500 * 0.45 + 1000 * 0.74 + (kwh_used - 1500) * 1.25
else:
    # Tudo acima de 2500 está na mesma faixa, então só else aqui
    out = 500 * 0.45 + 1000 * 0.74 + 1000 * 1.25 + (kwh_used - 2500) * 2.00

out = 1.2 * out
