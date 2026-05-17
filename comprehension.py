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
