numbers = [2, 7, 3, 9, 13]
total = 0

if (len(numbers) == 0):
    out = None
else:
    for i in numbers:
        total += i
    media = total/len(numbers)
    out = media

print(out)
