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


class Dj:
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

tiesto = Dj(
    name="Tiesto",
    age=55,
    equipment="Pioneer",
    discography=20,
    salary=30_000,
    genre="lite-house",
    male=True
)

avicci = Dj(
    name="Avicci",
    age=22,
    equipment="Pioneer",
    discography=40,
    salary=0,
    genre="adm",
    male=True
)

anna = Dj(**anna_data)


def validate_dj_data(data):
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

    return data


def add_dj(data):
    user_input = input("Enter new DJ's data: ")
    dj_data = user_input.split(",")
    validated_data = validate_dj_data(dj_data)

    if validated_data is not None:
        data.append(validated_data)
        return validated_data


def update_dj(data):
    print("Update DJ's data by format: name,age,equipment,discography,salary,genre,male: ")
    update_input = input("Enter DJ's new data:")
    update_data = update_input.split(",")
    validated_data = validate_dj_data(update_data)

    if validated_data is not None:
        data.append(validated_data)
        return validated_data


if __name__ == "__main__":
    djs = [tiesto, avicci, anna]
    allowed_options = "[add/list/names/delete/update/exit/]"

    while True:
        desision = input(f"What should I do?{allowed_options}: ")

        if desision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre")
            new_dj = add_dj(djs)
            if new_dj:
                print(f"DJ {new_dj['name']} is added!")

        elif desision == "list":
            for dj in djs:
                dj.show_short_details()

        elif desision == "names":
            data = [dj["name"] for dj in djs]
            pprint(data)

        elif desision == "delete":
            delete_name = input("Input DJ's name for delete: ")
            for dj in djs:
                if dj["name"] == delete_name:
                    djs.remove(dj)
                    print(f'DJ {delete_name} is deleted!')

        elif desision == "update":
            update_name = input("Input DJ's name for update: ")
            for dj in djs:
                if dj["name"] == update_name:
                    update_dj = update_dj(djs)
                    djs.remove(dj)
                    print(f'DJ {update_name} is updated!')

        elif desision == "exit":
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")