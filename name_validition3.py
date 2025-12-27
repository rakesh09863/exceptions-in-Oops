from name_validitionex2 import validation
from name_validition import ZeroLengthError,InvalidNameError
while(True):
    try:
        name=input('enter name:')
        res=validation(name)
    except ZeroLengthError:
        print('do not enter space')
    except InvalidNameError:
        print('{} is invalid name'.format(name))
    else:
        print(res)
        break