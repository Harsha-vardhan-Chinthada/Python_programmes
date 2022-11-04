def square(fun):
    def inner():
        result = fun()
        return result**2
    return inner


def double(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@square
@double
def num():
    return 10
print(num())