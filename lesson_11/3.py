def log(func):
    def inner(user):
        print(f"Connecting by {user}")
        return func(user)

    return inner


# log(visit_homepage)(user)
@log
def visit_homepage(user):
    print("Homepage")


@log
def visit_contacts(user):
    print("Contacts")


dima = "Dima"
admin = "Admin"

visit_homepage(dima)
visit_homepage(admin)

# callable = log(visit_homepage)(dima)
# callable = log(visit_homepage)(admin)
# callable = log(visit_contacts)(dima)
# callable = log(visit_contacts)(admin)