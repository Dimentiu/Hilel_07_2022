import json
import requests
from random import randint


class Pokemon:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # def __str__(self):
    #     return f"Hello, my name is {self.name}"

    def __repr__(self):
        return f"name: {self.name} weight: {self.weight}"

def get_random_id():
    return randint(1, 500)


def fetch_random_pokemon():
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    id_ = get_random_id()
    # url = base_url + id_
    url = "".join([base_url, str(id_)])
    response = requests.get(url)
    data = json.loads(response.text)

    return data


def get_pokemon():
    raw_data = fetch_random_pokemon()
    return Pokemon(
        name=raw_data["name"],
        weight=raw_data["weight"]
    )


pokemon = get_pokemon()

print(pokemon)