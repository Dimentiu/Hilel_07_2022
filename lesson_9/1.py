class Product:
    def __init__(self, name, color, price, amount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount

    def get_product_description(self):
        return f"{self.name}/{self.color}: {self.price} | {self.amount}"

    def show_description(self):
        print(f"Description: {self.get_product_description()}")


class Phone(Product):
    def __init__(self, name, color, price, amount, lte=False):
        # Product.__init__(self, name, color, price, amount)
        super().__init__(name, color, price, amount)
        self.lte = lte

    def get_product_description(self):
        additional = ", LTE" if self.lte else ""
        message = super().get_product_description()
        message += additional

        return message

    # def show_description(self):
    #     # if self.lte is True:
    #     #     additional = "LTE"
    #     # else:
    #     #     additional = ""
    #     additional = "LTE" if self.lte else ""
    #     print(f"Description: {self.name}/{self.color}: {self.price} | {self.amount}, {additional}")


class Laptop(Product):
    pass


single_product = Phone(name="Single product", color="red", price=700.0, amount=1)
single_product.show_description()


iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1, lte=False)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, lte=True)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1)

iphone13.show_description()
iphone7.show_description()
lenovo.show_description()