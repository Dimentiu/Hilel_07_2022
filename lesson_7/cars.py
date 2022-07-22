class CarShop:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def show_details(self):
        print(f"Car name: {self.name}\nPrice: {self.price}")


bmw = Car(name="bmw", price=30000)
vw = Car(name="vw", price=40000)


Car.show_details(bmw)
Car.show_details(vw)

bmw.show_details()
vw.show_details()


# class list:
#     def sort(self):
#         pass


# data = [3, 2, 1]
# data2 = [5, 6, 4]

# list.sort(data)
# list.sort(data2)

# data.sort()
# data2.sort()