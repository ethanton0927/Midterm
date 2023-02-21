def consecutive_ones(input):
    max_ones = 0
    count = 0
    for i in input:
        if i == '1':
            count += 1
            if count > max_ones:
                max_ones = count
        else:
            count = 0
    return max_ones