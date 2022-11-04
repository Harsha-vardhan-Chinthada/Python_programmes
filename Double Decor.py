def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner
def num():
    return 5
resultfun = (decor(num))
print(resultfun())

def decorfun(fun):
    def inner():
        result = fun()
        return result*3
    return inner
@decorfun
def num():
    return 5
print(num())

# practice
def decorfun1(fun):
    def inner():
        result = fun()
        return result*25
    return inner
@decorfun1
def num():
    return 4
print(num())











