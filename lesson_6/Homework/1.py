from pprint import pprint


tiesto = {
    "name": "Tiesto",
    "age": 55,
    "equipment": "Pioneer",
    "discography": 20,
    "salary": 30_000,
    "genre": "lite-house",
}
avicci = {
    "name": "Avicci",
    "age": 22,
    "equipment": "Pioneer",
    "discography": 40,
    "salary": 0,
    "genre": "adm",
}
anna = {
    "name": "Anna",
    "age": 24,
    "equipment": "Synth",
    "discography": 3,
    "salary": 3_000,
    "genre": "techno",
}


def validate_dj_data(data):
    if len(data) != 6:
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
    data = {
            "name": data[0],
            "age": data[1],
            "equipment": data[2],
            "discography": data[3],
            "salary": data[4],
            "genre": data[5],
        }
    
    return data


def add_dj(data):
    user_input = input("Enter new DJ's data: ")
    dj_data = user_input.split(",")
    validated_data = validate_dj_data(dj_data)

    if validated_data is not None:
        data.append(validated_data)
        return validated_data

def update_dj(data):
    print("Update Dj format: name,age,equipment,discography,salary,genre")
    update_input = input("Enter new DJ's data: ")
    update_data = update_input.split(",")
    validated_data = validate_dj_data(update_data)

    if validated_data is not None:
        data.append(validated_data)
        return validated_data

if __name__ == "__main__":
    djs = [tiesto, avicci, anna]
    allowed_options = "[add/list/names/exit/delete/update/]"
   

    while True:
        desision = input(f"What should I do?{allowed_options}: ")
        if desision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre")
            new_dj = add_dj(djs)
            if new_dj:
                print(f"DJ {new_dj['name']} is added!")
        elif desision == "list":
            pprint(djs)
        elif desision == "names":
            data = [dj["name"] for dj in djs]
            pprint(data)
        elif desision == "exit":
            print("Exiting...")
            break
        elif desision == "delete":
            delete_dj = input("Enter DJ name to delete:")
            for dj in djs:
                if dj["name"] == delete_dj:
                    djs.remove(dj)  
                    pprint(djs)
        elif desision == "update":
            update_name = input("Enter a name to replace:")
            for dj in djs:
                if dj["name"] == update_name:
                    update_dj = update_dj(djs)
                    djs.remove(dj)
                    print(f"DJ {update_name} is update")
                    
        else:
            print(f"Please use allowed options! {allowed_options}")
