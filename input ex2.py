from division import divop
from exception_in_oops_ex1 import DivisionByZero
while(True):
    try:
        a=int(input('enter first number:'))
        b=int(input('enter second number:'))
        try:
            res=divop(a,b)
        except DivisionByZero:
            print('do not enter zeros')
        else:
            print('div({}/{})={}'.format(a,b,res))
            break
    except ValueError:
        print('do not enter str,alphanum,symbols')
    finally:
        print('I am from finally block')

#phase3 handling of exception
