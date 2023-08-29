#!/usr/bin/python3

def magic_calculation(a, b):
    output = 0
    for j in range(2, 5):
        try:
            if j >= a:
                raise ValueError('Exceeded limit')
            output += a ** b / j
        except ValueError:
            output = b + a
            break
    return output

