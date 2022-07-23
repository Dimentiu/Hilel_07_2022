class Product:
    def __init__(self, name, color, price, amount, discount):
        self.name = name
        self.color = color
        self.price = price
        self.amount = amount
        self.discount = discount

    def get_product_description(self):
        return f"{self.name}/{self.color}: {self.price} | {self.amount}\Discount: {self.get_price()}"

    def show_description(self):
        print(f"Description: {self.get_product_description()}")

    def get_price(self):
        if self.discount:
            return self.price * (1-self.discount)
        

class Phone(Product):
    def __init__(self, name, color, price, amount, lte=False, discount=False):
        # Product.__init__(self, name, color, price, amount)
        super().__init__(name, color, price, amount, discount,)
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
    def __init__(self, name, color, price, amount, motherboard_type, material, lte=False, discount=False, ):
        super().__init__(name, color, price, amount, discount, )
        self.motherboard_type = motherboard_type
        self.material = material
    def get_show_details(self):
        return f"{self.name}/{self.color}: {self.price} | {self.amount}\Discount: {self.get_price()} | {self.motherboard_type} / {self.material}"
    
    def show_details(self):
        print(f"Description: {self.get_show_details()}")

iphone7 = Phone(name="iPhone 7", color="red", price=700.0, amount=1)
iphone13 = Phone(name="iPhone 13", color="black", price=2000.0, amount=2, lte=True, discount=0.2)
lenovo = Laptop(name="Lenovo", color="grey", price=3000.0, amount=1, motherboard_type ="Z590", material="plastic" ,discount=True)
lenovo2 = Laptop(name="Lenovo2", color="grey", price=2000.0, amount=1, motherboard_type="H310", material="plastic" ,discount=0.5)

iphone13.show_description()
iphone7.show_description()
lenovo.show_details()
lenovo2.show_details()
