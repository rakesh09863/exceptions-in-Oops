from name_validition import InvalidNameError,ZeroLengthError
def validation(name):
    if len(name) == 0:
        raise ZeroLengthError
    else:
        words=name.split()
        res=False
        for word in words:
            if not word.isalpha():
                res=True
                break
        if (res):
            raise InvalidNameError
        else:
            return '{} is valid name'.format(name)