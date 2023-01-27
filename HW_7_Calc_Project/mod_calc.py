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

def sqrt(a, b=None):
    if not b:
        return f'res = {a ** 0.5}'
        
    # return a ** b