# def foo(words):
#     # text = ""
#     # for word in words:
#     #     text += word
#     text = ", ".join(words)
#     print(text)
#
#
# def baz(arg):
#     print("I am BAZ!")
#
#
# def bar(arg, words):
#     arg(words)
#
#
# words = ["Hello", "Python", "Hillel"]

# bar(foo, words)
# bar(baz, None)


def is_authenticated(func):
    def inner(user):
        if user["username"] == "admin" and user["password"] == "admin123":
            print("User is authenticated")
            return func()
        else:
            print("User is NOT authenticated")
    return inner


@is_authenticated
def view_homepage():
    print("Home page")


@is_authenticated
def view_contacts():
    print("Contacts page")


dima = {"username": "dima", "password": "dima123"}
admin = {"username": "admin", "password": "admin123"}

view_homepage(dima)
view_homepage(admin)
view_contacts(dima)
view_contacts(admin)

# is_authenticated(view_homepage, dima)
# is_authenticated(view_homepage, admin)()
# is_authenticated(view_contacts, dima)
# is_authenticated(view_contacts, admin)