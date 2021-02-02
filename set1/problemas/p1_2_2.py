numbers = [60, 6000]
product = 1
arr_length = len(numbers)

if (arr_length == 0):
    out = None
else:
    for i in range(0, arr_length):
        product *= numbers[i]

    geometric_mean = (product ** (1/arr_length))
    out = geometric_mean
    print(out)
