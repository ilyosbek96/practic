'''comprehension
(1) comprehension o'zi nima va list comprehension
(2) set va dictionary comprehension
'''
print("======== comprehension o'zi nima va list comprehension ========")
# comprehension degani spread operator

''' Comprehensionni umumiy qolipi yani sintaksisi
    a) *iterable takrorlanish
    b) expression > for item in iterable
    c) expression > for item in iterable <condition>
'''

# listllar bilan bog'liq comprehensionlar
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
print("list_numbers:", list_numbers)
# list nuber birxil objectmi degani (ture) (false) qaytaradi
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))
print("="*25)

#     b) expression > for item in iterable
# tuplelardan iborad list yashash
people = [("Robert", 20), ("ILYOSBEK", 29), ("JOSEPH", 25)]
list_people = [person[0]
               for person in people]  # [1] qilinsa raqamlarni olib beradi
print("list_people:", list_people)

# c) expression > for item in iterable <condition>
cars = [
    ("Ferari", 78),
    ("BMW", 109),
    ("Mercades", 100),
    ("Audi", 116),
    ("Porche", 50)
]
list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars:", list_cars)

print("======== set va dictionary comprehension  ========")
# list yaratish
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
# set orqalik chaqirib olsih yai set takroriy bo'lgan sonlarni 1donasini olib beradi
# set objectni yaratamiz
# {qavus ochiladi} va *number yoziladi bu itareble takrorlash va yoyib berish
set_numbs = {*numbs}
print("set_numbs:", set_numbs)

print("===== b) expression > for item in iterable =====")
# b) expression > for item in iterable
dict_people = {person[0]: person[1] for person in people}
print("dict_people:", dict_people)
print("===== c) expression > for item in iterable <condition> =====")
# c) expression > for item in iterable <condition>
dict_people1 = {person[0]: person[1] for person in people if person[1] > 20}
print("dict_people1:", dict_people1)

#
