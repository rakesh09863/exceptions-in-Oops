from division import divop
from exception_in_oops_ex1 import DivisionByZero
while(True):
    try:
        a=int(input('enter first number:'))
        b=int(input('enter second number:'))
        res=divop(a,b)
    except DivisionByZero:
        print('do not enter zeros')
    except ValueError:
        print('do not enter str,alphanum,symbols')
    else:
        print('div({}/{})={}'.format(a,b,res))
        break
    finally:
        print('I am from finally block')

#phase3 handling of exception



