class Pizza:
    def __init__(self, tomato=0, meat=0, cheese=0, pineapple=0):
        self.tomato = tomato
        self.meat = meat
        self.cheese = cheese
        self.pineapple = pineapple

    def show_description(self):
        print(f"Pizza(tomato: {self.tomato}, meat: {self.meat}, cheese: {self.cheese}, pineapple: {self.pineapple})")


class PizzaShop:
    pizzas = []

    @classmethod
    def cook(cls, pizza, box=False):
        print(f"cooking pizza")
        pizza.show_description()
        if box is True:
            print("Packing into the box")
        cls.pizzas.append(pizza)


peperony = PizzaShop.cook(Pizza(**{"tomato": 2, "meat": 3, "cheese": 1}), True)
havay = PizzaShop.cook(Pizza(tomato=2, meat=3, pineapple=1))

# for pizza in PizzaShop.pizzas:
#     pizza.show_description()