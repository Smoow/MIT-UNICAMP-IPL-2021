interest_rate = 0.05
initial_cash = 500000.0
hand_cash = initial_cash
final_cash = 1000000.0
years = 1

while (hand_cash <= final_cash):
    hand_cash = initial_cash * ((1 + interest_rate) ** years)
    out = years
    years += 1

print(out)
