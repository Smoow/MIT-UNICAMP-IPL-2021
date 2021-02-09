year = 2017
month = 1  # 1 = Janeiro, 2 = Fevereiro, ..., 12 = Dezembro
day = 9

if month == 1:
    y1 = year - 1
    m1 = month + 12
elif month == 2:
    y1 = year - 1
    m1 = month + 12
else:
    y1 = year
    m1 = month

y2 = y1 % 100
c = y1 // 100

w = (day + (13 * (m1 + 1) // 5) + y2 + y2 // 4 + c // 4 - 2*c) % 7

out = w
