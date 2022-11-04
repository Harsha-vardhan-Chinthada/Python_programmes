def fun(x, *args, **kwargs):
    print(x)
    for each_arg in args:
        print(each_arg)
    for key,value in kwargs.items():
        print(key,value)
fun(109, 12, 23, Name = "Harsha", sal = 100000)