def my_func(value):
    def wrapper():
        print('Who Let the Dogs Out')
        value()
        user_input = input()
        if user_input.isdigit():
            print(f"{user_input} The number of arguments is not correct!")
            return None
        print(user_input, 'Let the Dogs Out')   
    return wrapper

def say_way():
    pass

say_way = my_func(say_way)
say_way()

    