import json
from pprint import pprint


class Dj:
    # This is a list of all djs
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

    @property
    def as_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "equipment": self.equipment,
            "discography": self.discography,
            "salary": self.salary,
            "genre": self.genre,
            "male": self.male,
        }

    @classmethod
    def add(cls):
        print(
            "Update DJ's data by format: name,age,equipment,discography,salary,genre,male: "
        )
        user_input = input("Enter new DJ's data: ")
        dj_data = user_input.split(",")
        new_dj = cls.validate(dj_data)

        if new_dj is not None:
            cls.djs.append(new_dj)
            return new_dj

    @classmethod
    def delete(cls, name):
        for dj in cls.djs:
            if dj.name == name:
                index = cls.djs.index(dj)
                del cls.djs[index]
                return True
        return False

    @classmethod
    def update(cls, name):
        selected_dj = None
        for dj in cls.djs:
            if dj.name == name:
                selected_dj = dj.name
                break

        if selected_dj is None:
            return

        print(
            "Update DJ's data by format: name,age,equipment,discography,salary,genre,male: "
        )
        update_input = input("Enter DJ's new data:")
        update_data = update_input.split(",")
        new_dj = cls.validate(update_data)

        if new_dj is None:
            return None

        deleted = cls.delete(selected_dj)
        if deleted:
            cls.djs.append(new_dj)
            return new_dj

    @classmethod
    def list(cls):
        for dj in Dj.djs:
            dj.show_short_details()

    @classmethod
    def names(cls):
        data = [dj.name for dj in Dj.djs]
        pprint(data)

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
    def read_from_file(cls):
        FILENAME = "djs.json"

        with open(FILENAME) as file:
            data = json.load(file)["results"]

        djs = [cls(**payload) for payload in data]
        # djs = []
        # for payload in data:
        #     djs.append(cls(**payload))

        return djs

    @classmethod
    def update_file(cls):
        FILENAME = "djs.json"
        formatted_djs = [dj.as_dict for dj in cls.djs]

        data = {"results": formatted_djs}
        data_as_json = json.dumps(data, indent=4)

        with open(FILENAME, "w") as file:
            file.write(data_as_json)


if __name__ == "__main__":
    # NOTE: Populate djs list
    extracted_djs: list = Dj.read_from_file()
    Dj.djs = extracted_djs

    allowed_options = "[add/list/names/delete/update/exit/]"

    while True:
        decision = input(f"What should I do?{allowed_options}: ")

        if decision == "list":
            Dj.list()
        elif decision == "names":
            Dj.names()
        elif decision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre,male")
            new_dj = Dj.add()
            if new_dj:
                print(f"DJ {new_dj.name} is added!")
        elif decision == "update":
            name = input("Input DJ's name for update: ")
            updated_dj = Dj.update(name)
            if updated_dj:
                print(f"DJ {updated_dj.name} is updated!")
        elif decision == "delete":
            delete_name = input("Input DJ's name for delete: ")
            deleted = Dj.delete(delete_name)
            if deleted is True:
                print(f"DJ {delete_name} is deleted!")
        elif decision == "exit":
            print("♻︎ Updating the file...")
            Dj.update_file()
            print("✅ File saved")
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")