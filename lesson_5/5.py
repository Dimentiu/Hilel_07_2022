person = ("John", "Doe", "63-27-09", "New-York", 33, 175, 89)

# name, _, phone, _, age, *_ = person
*_, weigh = person

print(weigh)
# print(phone)
# print(age)
# print(_)
