print("=========== ITERABLE OBJECTS & RANGE ==========")
# ITERABLE > takrorlanish xususiyatiga ega bo'lgan object degani

# ITERABLE > string dict tuple list range map filter

# ===================== STRING OBJECTI =================
text = "MIT"
for letter in "MIT":
    print(f"the letter: {letter}")
# ===================== STRING OBJECTI =================
range_obj = range(3)
print("range_obj:", range_obj)
for ele in range_obj:
    print(f"the element: {ele}")

print("=========== DICTIONARY ==========")
#  DICTIONARY > JSON OBJECT desaxam bo'ladi
person = {"name": "ILYOSBEK", "age": 25, "single": True}
#  DICTIONARY > function orqalikxam xosil qilsa bo'ladi
person_obj = dict(name="NOE", age=29, single=True)
print(f"the person: {person}")  # f > farmat string
print(f"the person_obj: {person_obj}")

name = person_obj["name"]
print("name:", name)
yosh = person_obj["age"]
print("yosh:", yosh)
single = person["single"]
print("single:", single)

# method: get() get bu methodni nomi
name = person.get("name")
hobby = person.get("hobby", )
balance = person.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} va balance: {balance}")
# iterableni tekshirish
# olib tashlash (del) orqalik
del person["single"]
for key in person:
    print(f"the key: {key} => value {person[key]}")
# get orqalik valueni tekshirish
print(f"the key: {key} => value {person.get(key)}")
