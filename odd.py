def sum(lbound, rbound, divisor, modulus):
    sum = 0
    for i in range(lbound, rbound + 1):
        if i % divisor == modulus:
            sum = sum + i

    return sum

def sum_odd(lbound, rbound):
    return sum(lbound, rbound, 2, 1)
