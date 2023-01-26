from logg import logging


def sum(a, b):
    return f'res = {a + b}'

def sub(a, b):
    return f'res = {a - b}'

def mul(a, b):
    return f'res = {a * b}'

def div (a, b):
    if b == 0:
        return 'Division is impossible'
    return f'res = {a / b}'

def int_div(a, b):
    if b == 0:
        return 'Division is impossible'
    return f'res = {a // b}'

def rem_div(a, b):
    if b == 0:
        return 'Division is impossible'
    return f'res = {a % b}'

def pow(a, b):
    return f'res = {a ** b}'

def pow_data(num_1, num_2=None):
    if not num_2:
        return num_1 ** 0.5
    return num_1 ** num_2