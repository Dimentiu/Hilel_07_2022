from pprint import pprint as print
from typing import Any, Callable


def save_to_db(address: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            data = func(*args, **kwargs)
            print(f"{data} is saving to the database {address}...")
            return data

        return inner

    return wrapper


@save_to_db(address="10.0.0.1")
def get_user_info(fields: list[str]) -> dict[str, Any]:
    result = {}
    for field in fields:
        data = input(f"Please enter your {field}: ")
        result[field] = data
    return result


@save_to_db(address="10.0.0.2")
def get_device_info() -> dict[str, Any]:
    model = input("Please enter your model: ")
    year = int(input("Please enter the year: "))
    result = {
        "model": model,
        "year": year,
    }
    return result


def main():
    user_fields = ["name", "surname"]
    user_info = get_user_info(fields=user_fields)
    device_info = get_device_info()

    print(f"User info: {user_info}")
    print(f"Device info: {device_info}")


if __name__ == "__main__":
    main()