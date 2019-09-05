import random

def flip():
    return random.random() > 0.5

def random_number(n):
    if n == 1:
        return 0
    binary_len = len('{0:0b}'.format(n)) - 1
    
    random_n = ''
    for i in range(binary_len):
        random_n += '1' if flip() else '0'
    
    return int(random_n, 2)


print(random_number(500))
print(random_number(1))
print(random_number(1000))
print(random_number(3))
print(random_number(4))