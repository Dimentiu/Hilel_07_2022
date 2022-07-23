class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    text = "Gav gav"


class Cat(Animal):
    text = "Miau miau"


class Mouse(Animal):
    text = "I can not speak"


def say(animal):
    print(f"{animal.name} says {animal.text}")


tom = Cat(name="Tom")
butch = Cat(name="Butch")
spike = Dog(name="Spike")
jarry = Mouse(name="Jarry")

say(tom)
say(butch)
say(spike)
say(jarry)