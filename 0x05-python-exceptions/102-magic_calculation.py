#!/usr/bin/python3

def magic_calculation(x, y):
    output = 0
    for j in range(2, 5):
        try:
            if j >= x:
                raise ValueError('Exceeded limit')
            output += x ** y / j
        except ValueError:
            output = y + x
            break
    return output

