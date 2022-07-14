from pprint import pprint

tiesto = {
    "name": "Tiesto",
    "age": 55,
    "equipment": "Pioneer",
    "discography": 20,
    "salary": 30_000,
    "genre": "lite-house"
}
avicci = {
    "name": "Avicci",
    "age": 22,
    "equipment": "Pioneer",
    "discography": 40,
    "salary": 0,
    "genre": "adm"
}
anna = {
    "name": "Anna",
    "age": 24,
    "equipment": "Synth",
    "discography": 3,
    "salary": 3_000,
    "genre": "techno"
}

djs = [tiesto, avicci, anna]

# results = []
# for dj in djs:
#     if dj["age"] > 30:
#         results.append(dj)

results = [dj for dj in djs if dj["age"] > 30]

pprint(results)
