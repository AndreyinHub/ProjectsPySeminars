from logg import logging
from excep import check_complex1, check_complex2

import mod_calc as c

def menu():
    print('Calculator welcomes you!')
    while True:
        rat_com = input('Working with: \n'
                   '1 - rational\n'
                   '2 - complex\n'
                   '0 - exit\n'
                   'Enter selected digit: '
                   )
        match rat_com:
            case '1':
                menu_rat()
            case '2':
                menu_com()
            case '0':
                logging.info("Stop program.")
                break
            case _:
                logging.warning("Main menu, wrong item selected.")
                print('Error. The menu item is not recognized. Try again!')
                break


def get_numder():
    while True:
        try:
            n = float(input('Enter number: '))
            return n
        except ValueError:
            input('Error. Enter number: ')


def menu_rat():
    logging.info(f"Start menu calc. With data type =  rational.")
    while True:
        act = input('Select an operation\n'
                  '1 - "sum +"\n'
                  '2 - "sub -"\n'
                  '3 - "mul *"\n'
                  '4 - "div /"\n'
                  '5 - "div //"\n'
                  '6 - "div %"\n'
                  '7 - "pow **"\n'
                  '8 - "scrt **0.5"\n'
                  '0 -  previos menu\n'
                  'Enter number selected operation: '
                  )
        
        n1 = get_numder()
        n2 = get_numder()
        
        match act:
            case '1':
                logging.info(f"Sum: {n1} + {n2} = {c.sum(n1,n2)}")
                return print(f'{n1} + {n2} = {c.sum(n1,n2)}')
            case '2':
                logging.info(f"Sub: {n1} - {n2} = {c.sub(n1,n2)}")
                return print(f'{n1} - {n2} = {c.sub(n1,n2)}')
            case '3':
                logging.info(f"Mul: {n1} * {n2} = {c.mul(n1,n2)}")
                return print(f'{n1} * {n2} = {c.mul(n1,n2)}')
            case '4':
                logging.info(f"Div: {n1} / {n2} = {c.div(n1,n2)}")
                return print(f'{n1} деление {n2} = {c.div(n1,n2)}')
            case '5':
                logging.info(f"Div int: {n1} // {n2} = {c.int_div(n1,n2)}")
                return print(f'{n1} деление целочисленное на {n2} = {c.int_div(n1,n2)}')
            case '6':
                logging.info(f"Div rem: {n1} % {n2} = {c.rem_div(n1,n2)}")
                return print(f'{n1} деление без остатка на {n2} = {c.rem_div(n1,n2)}')
            case '7':
                logging.info(f"Pow: {n1} ** {n2} = {c.pow(n1,n2)}")
                return print(f'{n1} в степени {n2} = {c.pow(n1,n2)}')
            case '8':
                logging.info(f"Sqrt({n1}) = {c.sqrt(n1)}")
                return print(f'квадратный корень числа {n1} = {c.sqrt(n1)}')
            case '0':
                break
            case _:
                print('Error')
                logging.warning("Previous menu, wrong item selected.")
                break


def menu_com():
    logging.info(f"Start menu calc. With data type =  complex.")
    while True:
        ac_t = input('Select an operation\n'
                  '1 -  "sum+"\n'
                  '2 -  "sub-"\n'
                  '3 -  "mul*"\n'
                  '0 -  previos menu\n'
                  'Enter number selected operation: '
                  )

        n = check_complex1()
        n1 = check_complex2()
        n2 = check_complex1()
        n3 = check_complex2()
        nn = complex(n, n1)
        mm = complex(n2, n3)

        match ac_t:
            case '1':
                logging.info(f'{nn} + {mm} = {c.sum(nn,mm)}')
                return print(f'{nn} + {mm} = {c.sum(nn,mm)}')
            case '2':
                logging.info(f'{nn} - {mm} = {c.sub(nn,mm)}')
                return print(f'{nn} - {mm} = {c.sub(nn,mm)}')
            case '3':
                logging.info(f'{nn} * {mm} = {c.mul(nn,mm)}')
                return print(f'{nn} * {mm} = {c.mul(nn,mm)}')
            case '0':
                break
            case _:
                logging.warning("Previous menu, wrong item selected.")
                print('Error')
                break



