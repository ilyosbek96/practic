''' LIST
    (1) Working with lists
    (2) List method
    (3)Lambda Function
    (4) Enumerate, map and filter
'''

print("=====================  (1) Working with lists ================================")
# Java/PHP/NodeJS array => Python list
# LIST 2 XIL USULDA QURILADI   (1)literal,   (2)constructor

# (1) literal
# [dictionary] li literal usulda tash qilish
person = {"name": "JACK", "age": 25}  # dictionar
people = ("Andrew", "John", "Leo")  # [tuple] literal usulda tash qilish
groups = ["MIT", "FLEX", "DEVEX", "MG"]  # literal uslubida list tash qilish
for team in groups:  # for orqali qolga olamiz
    print(f"the team: {team}")

# (2)constructor
result = list("Hello World!")
print(f"the result: {result} and size: {len(result)}")


print("-------")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]  # [0, 2] 2 kirmaydi yarm interval yani [0,1 kiradi degani)
c = fruits[::3]  # 3 qadam sakraydi
d = fruits[::-1]  # teskari holat

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("=====================    (2) List method ================================")
# method > append() insert() pop() remove() clear() sort() mutable arrayga tasrkoratadi                         index() Immutable -tasr korsatmaydi

# Mutable
letters = ["a", "d", "b"]  # harfklardan iborat array

letters.append("c")  # oxiridan qoshadi
print(f"the append result: {letters}")

letters.insert(0, "z")  # oldidan qoshadi
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop oxiridan ayiradi
print(f"the pop result1: {result1} and letters {letters}")

result2 = letters.pop(0)  # pop bunda boshidan ayiradi
print(f"the pop result2: {result2} and {letters}")


print("---------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)


animals.remove("lion")  # udalit qilish
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)  # delete aytgan sonni

exist = animals.index("cat")  # nechinchi indexni topadi
print("cat exist", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")


print("----sort------")  # tartiblab yozib beradi
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default:", numbers)  # kichik qiymatdan kottaga qarab
numbers.sort(reverse=True)
print("sort reverse=True:", numbers)  # kotta qiymatdan kichikga  qarab


print("--- Immutable sorted index() --")
# Immutable > sorted  function & index() method
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)  # bunda yangi new_numbs ozgargan
print(f" the sorted numbs: {numbs} and new_numbs: {new_numbs}")

print("====== Lambda Function ======")
# lambdamiz bu qichik anonymous function

# function tuzvolamiz

# eng sodda lambda functioni


def calculate(x, y): return x * y


natija = calculate(5, 10)
print("natija:", natija)

# listimiz mavjun uni ichid ismlar
people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
]
# sort qilish yani yoshiga nisbatan lambda orqalik
people.sort(key=lambda person: person[1])
print("people:", people)

print("====== Enumerate, map and filter ======")
# Enumerate > bir vaqtning o'zida value xamda indexsini olishda yordam beradi
animals = ["dog", "cat", "fidh"]  # bu list
for element in enumerate(animals):
    print("element:", element)
print("="*15)
for (index, value) in enumerate(animals):
    # listda esa index xamda value bo'ladi
    print(f"the index: {index} and value: {value}")

print("="*15)
# siminal in dictionaries bu => (json object)
car_obj = dict(brand="BMW", year=2026)  # dict
# dictionariesni items methodinii xosil qilib arrayga key va valuelarni tuple qilib yoyib beradi
natija = car_obj.items()
print("natija:", natija)
for (key, value) in natija:  # dictionaries objectda key value deyiladi (bo'ladi)
    print(f"the key: {key} and value: {value}")


print("="*15)
# map
cars = [
    ("Ferari", 70),
    ("Tayota", 87),  # bular xammasi tuple ko'rinishda
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

# yangi array yaratamiz
new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_cars(1)", new_cars)

# map objecti orqaalik lambdani xosil qilyapmiz
# to'gridan to'g'ri ko'rib bo'lmaydi zip ko'rinishda bo'lib qoladi
natija_map = map(lambda car: car[0], cars)
print(f"the natija_map: {natija_map} and type: {type(natija_map)}")

# natijani ko'rish uchun list ko'rinishiga olib o'tish kerak
new_cars = list(natija_map)  # mapni listsga argument qilib beryapmiz
print("new_cars(2)", new_cars)


# fiter object
natija_filter = filter(lambda car: car[1] > 80, cars)
print(f"the natija_filter: {natija_filter} and type: {type(natija_filter)}")
print(list(natija_filter))
