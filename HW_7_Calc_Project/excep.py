def is_number_div(x, y):
    if y == '0':
        return False
    while True:
        try:
            float(x), float(y)
            return True
        except ValueError:
            return False


def is_number_all(x, y):
    while True:
        try:
            float(x), float(y)
            return True
        except ValueError:
            return False


def check_complex1():
    n = input('Enter real part: ')
    while not n.isdigit():
        print('Error')
        n = input('Enter once again: ')
    return int(n)


def check_complex2():
    n = input('Enter imaginary number: ')
    while not n.isdigit():
        print('Error')
        n = input('Enter once again: ')
    return int(n)
