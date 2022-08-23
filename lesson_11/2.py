def connect_to_postgres():
    # NOTE: ...
    print("PostgreSQL 13.3")


def connect_to_mysql():
    # NOTE: ...
    print("MySQL 8")


def log(func):
    print("Connected")
    return func

data = log(connect_to_postgres)

print(data)
data()
Footer
© 2022 GitHub, Inc.