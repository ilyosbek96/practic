''' TUPLE
(1) TUPLE  o'zi nima: typle va list
(2) AGRUMENTLARNI yoyish (unpacking)
(3)
'''
print("===== TUPLE  o'zi nima: typle va list =====")
# JAVA/PHP/NODEJS dagi array => pythonda list deyiladi

# literal => yani to'g'ridan to'g'ri qurish degani
numbs = [3, 5, 1, 2]
# print(numbs)

# constructor
letters = list("salom dunyo")  # list functionnini qurib letterni xosil qildik
# print(letters)

mevalar = ["olma", "banan", "uzum", "gilos"]
print("oldingi mevalar:", mevalar)

# yyangi mevaga o'zgartirish
mevalar[2] = "limon"
print("yangi mevalar:", mevalar)

# TUPLE qiymatini hechqachon o'zgartirsa bo'lmaydi
hayvonlar = ("kuchuk", "mushuk", "baliq", "sher")
tuple_obj = ("mit", 100, True, None)

print(hayvonlar[0])
# hayvonlar[0] = "ot"

print("===== AGRUMENTLARNI yoyish =====")
gruppa = ["MIT", "FLEXY", "DEVEX", "MG"]
# yoyish uchun maxsus (qavus) qo'yiladi va ichiga yoziladi
# birlashtirish uchun esa * harf misol(z) yozsaxam bo'ladi print qilinganda list orqalik terminalga chiqadi yani [shuni ichida]
(x, y, z, a) = gruppa
print(f"the x: {x} and y: {y}")

# *argument (args) > tuple xisoblanadi


def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


# call
calculate(1, 7, 2, 3)
print("="*15)
calculate(0, 2, 300)
print("="*15)
calculate(5, 7)


print("-------------")
# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi I am {kwargs["name"]} and I am{kwargs["age"]} year old! ")


# Call
introduce(name="Jastin", age=25)
introduce(name="Shawn", age=25, singler=True)
print("-------------")


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# Call
greeting("hi", True, 10, name="John", age=22)


print("========= (3) ZIP  =======")  # Iterable object zip
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped:", zipped)
resilt = list(zipped)
print(f"the result: {resilt}")
