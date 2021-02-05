def largest_number(input_list):
    best_so_far = -100**99

    if (len(input_list) < 1): return None
    else:
        for i in range(len(input_list)):
            if input_list[i] > best_so_far:
                best_so_far = input_list[i]

    return best_so_far

def second_largest_number(input_list):
    if (len(input_list) < 2):
        return None
    else:
        tmp = -100**99
        largest = largest_number(input_list)

        if (input_list.count(largest) > 1): return largest
        else: 
            for i in input_list:
                if i > tmp and i != largest:
                    tmp = i
         
        return tmp
