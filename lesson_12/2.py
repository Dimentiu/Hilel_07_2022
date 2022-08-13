from fileinput import close


# class open:
#     def __init__(self, path, encoding) -> None:
#         self.path = path
#         self.file = IO...

#     def __enter__(self):
#         return IOText

#     def __exit__(self, *args, **kwargs):
#         self.file.close()

FILENAME = "users.txt"

class User:
    def get_name(self):
        print("Dima")


class Test:
    def __enter__(self):
        # return "Message"
        return User()

    def __exit__(self, *args, **kwargs):
        print("Bye!!!")


# with Test() as msg:
#     print(msg)
        
with Test() as user:
    user.get_name()


# with open(FILENAME, mode="r", encoding="utf-8") as f:
#     data = f.readlines()
#     print(data)


# file_2 = open(FILENAME, mode="w", encoding="utf-8")
# file_2.write("Hello Python")
# file_2.close()

# file_2 = open(FILENAME, mode="w", encoding="utf-8")
# file_2.write("Hello Python 2")
# file_2.close()

# file = open(FILENAME, mode="r", encoding="utf-8")
# data = file.read()
# lines = data.split("\n")
# print(lines)
# file.close()



# file_2 = open(FILENAME, mode="r", encoding="utf-8")
# data_2 = file_2.read()
# lines_2 = data_2.split("\n")
# print(lines_2)
# file_2.close()