
class Car:
    def __init__(self, name, year, manufacturer, engine, color, price) -> None:
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def show_details(self):
        print(f"Car name: {self.name}|Price: {self.price}")
        
    def show_details_full(self):
        print(f"{self.name}/{self.year}: {self.manufacturer} | {self.engine}|{self.color}/{self.price}")
        


class Book:
    def __init__(self, title, year, publisher, genre, author, price) -> None:
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def details_book(self):
        print(f"book title: {self.title}|Price: {self.price}")
    def details_book_full(self):
        print(f"{self.title}/{self.year}: {self.publisher} | {self.genre}|{self.author}/{self.price}")

class Stadium:
    def __init__(self, name, date, country, city,) -> None:
        self.name = name
        self.date = date
        self.country = country
        self.city = city
       
    def details_Stadium(self):
        print(f"football stadium: {self.name}|Country: {self.country}")
    def details_Stadium_full(self):
        print(f"{self.name}/{self.date}: {self.country} | {self.city}")


volvo = Car(name="volvo", year = "2012", manufacturer = "Poland", engine = "2.0 TDI", color = "red", price = "20000")
volvo.show_details_full()
volvo.show_details()

space = Book(title = "space", year = "1985", publisher = "India",genre = "scientific", author = "shrn", price = "100")
space.details_book_full()
space.details_book()

DneprArena = Stadium(name="DneprArena", date = "2000", country = "Ukraine", city = "Dnipro")
DneprArena.details_Stadium_full()
DneprArena.details_Stadium()

