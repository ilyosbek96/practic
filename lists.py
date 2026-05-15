''' LIST
    (1) Working with lists
    (2) List method
    (3)Lambda Function
    (4) Enumarte, map and filter
'''

print("=====================  (1) Working with lists ================================")
# Java/PHP/NodeJS array => Python list
# LIST 2 XIL USULDA QURILADI   (1)literal,   (2)constructor

# (1) literal
# [dictionary] li literal usulda tash qilish
person = {"name": "JACK", "age": 25}
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
b = fruits[0:2]  # [0, 2] 2 kirmaydi
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
