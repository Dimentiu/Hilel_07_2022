def parabol(x, *blabla, **kwargs):
    print(blabla)
    print(kwargs)
    return x ** 2


x = 2

result = parabol(x=2, 123, "qwe", name="Dima")

print(result)
