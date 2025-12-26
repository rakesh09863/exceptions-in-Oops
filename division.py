from exception_in_oops_ex1 import DivisionByZero
def divop(a,b):
    if b==0:
        raise DivisionByZero
    else:
        return a/b

#phase2:We develop Business logic (problem solving logic)
#and we hit exception if possible in the case of wrong Input
#we give output in the case of Valid input