p_d = 13
total_area = p_d ** 2

generator = []
circles_inside = []
counter = 0

len_neg = int(((p_d - 1) / 2) - (p_d - 1))
len_pos = int(((p_d - 1) / 2))

for i in range(len_neg, 1, 1):
    for j in range(len_neg, 1, 1):
        generator.append([i, j])

for i in range(1, len_pos+1, 1):
    for j in range(1, len_pos+1, 1):
        generator.append([i, j])

for i in range(1, len_pos+1, 1):
    for j in range(len_neg, 1, 1):
        generator.append([i, j])

for i in range(len_neg, 1, 1):
    for j in range(1, len_pos+1, 1):
        generator.append([i, j])

while (counter < len(generator)):
    if( (((generator[counter][0] ** 2) + generator[counter][1] ** 2) ** 0.5) <= p_d/2 ): 
        circles_inside.append(generator[counter])
    # print(counter)
    counter += 1

out = (len(circles_inside)/total_area) * 4
print(out)
