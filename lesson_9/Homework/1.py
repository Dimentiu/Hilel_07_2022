from pprint import pprint

anna_data = {
    "name": "Anna",
    "age": 24,
    "equipment": "Synth",
    "discography": 3,
    "salary": 3_000,
    "genre": "techno",
    "male": False
}
tiesto_data = {
    "name": "Tiesto",
    "age": 55,
    "equipment": "Pioneer",
    "discography": 20,
    "salary": 30_000,
    "genre": "lite-house",
    "male": True
}
avicci_data = {
    "name": "Avicci",
    "age": 22,
    "equipment": "Pioneer",
    "discography": 40,
    "salary": 0,
    "genre": "adm",
    "male": True
}


class Dj:
    djs = []

    def __init__(self, name, age, equipment, discography, salary, genre, male):
        self.name = name
        self.age = age
        self.equipment = equipment
        self.discography = discography
        self.salary = salary
        self.genre = genre
        self.male = male

    def show_short_details(self):
        if self.male is True:
            message = "He is"
        else:
            message = "She is"
        print(f"{message} {self.name}, {self.age} years old")

    @classmethod
    def add(cls):
        user_input = input("Enter new DJ's data: ")
        dj_data = user_input.split(",")
        new_dj = cls.validate(dj_data)

        if new_dj is not None:
            cls.djs.append(new_dj)
            return new_dj
    
    @classmethod
    def validate(cls, data):
        if len(data) != 7:
            print("The number of arguments is not correct!")
            return None

        if data[0].isdigit():
            print(f"{data[0]} is digit")
            return None

        for element in [data[1], data[3], data[4]]:
            index = data.index(element)
            if element.isdigit():
                data[index] = int(element)
            else:
                print(f"{element} is not a digit")
                return None

        if not data[5].isalnum():
            print(f"{data[5]} is not an alnum")
            return None

        return cls(*data)

    @classmethod
    def update(cls, data):
        print("Update Dj format: name,age,equipment,discography,salary,genre")
        update_input = input("Enter new DJ's data: ")
        update_data = update_input.split(",")
        validated_data = cls.validate(update_data)

        if validated_data is not None:
            cls.djs.append(validated_data)
            return validated_data
   
    @classmethod
    def list(cls):
        for dj in Dj.djs:
            dj.show_short_details()

    @classmethod
    def names(cls):
        data = [dj.name for dj in Dj.djs]
        pprint(data)


if __name__ == "__main__":
    tiesto = Dj(**tiesto_data)
    avicci = Dj(**avicci_data)
    anna = Dj(**anna_data)

    # Populate djs list
    Dj.djs = [tiesto, avicci, anna]

    allowed_options = "[add/list/names/delete/update/exit/]"

    while True:
        desision = input(f"What should I do?{allowed_options}: ")

        if desision == "list":
            Dj.list()
        elif desision == "names":
            Dj.names()
        elif desision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre,male")
            new_dj = Dj.add()
            if new_dj:
                print(f"DJ {new_dj.name} is added!")     
        elif desision == "update":
            name = input("Input DJ's name for update: ")
            updated_dj = Dj.update(name)
            if updated_dj:          
                print(f'DJ {updated_dj.name} is updated!')
        elif desision == "delete":
            delete_name = input("Input DJ's name for delete: ")
            deleted = Dj.delete(name)
            if deleted is True:
                print(f'DJ {delete_name} is deleted!')
        elif desision == "exit":
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")