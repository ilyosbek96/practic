''' FUNCTIONS
  (1) DEFINE VA CALL
  (2) PARAMETR VA ARGUMENT
  (3) KEYWORD & DEFAULT ARGUMENTLAR
  (4) SCOPE
'''
print("======== DEFINE VA CALL ========")
# build in functionlar > type() print()
# FUNCTION ㅡmalumbir vazifani ishga tushurib berodigon code block
# instead of block {} javada qullik qavush orqalik qilinadi
# pythonda esa ikkita nuqta orqalik yani > ( : ) = (INDENTATION) shu belgi orqalik
# INDENTATION automat joy tashlab beradi

# define / qurib olish


def greet(a):
    print(f"how do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"hi {b}"


# call / chaqirib olish
natija = greet('ILYOSBEK')
print("natija:", natija)

natija1 = greeting('MIT')
print("natija1:", natija1)

print("======== KEYWORD & DEFAULT ARGUMENTLAR ========")
# DEFINE

# ==================== KEYWORD ARGUMENTLAR ====================


def give_greet(name, age):
    print("give_greet ishga trushdi")
    return f"salom {name}, sizning yoshingiz {age} yoshda"


# calll
natija2 = give_greet(name="Ilyosbek", age=29)  # KEYWORD argument
print("natija2:", natija2)

# ==================== DEFAULT ARGUMENTLAR ====================


def give_gree(name, age=30):  # DEFAULT argument
    print("give_gree ishga trushdi")
    return f"salom {name}, sizning yoshingiz {age} yoshda"


natija3 = give_gree("Ilyosbek")
print("natija3:", natija3)

print("========== SCOPE ==========")
d = 100  # 3chi izlaydi

# DEFINE


def calculate(e, f):  # 2 hi izlaydi buyerdaxam bo'lmasa tashqaridan izlaydi
    g = e * f  # 1chi izlaydi
    print(f"the g value: {g}")


# call
calculate(5, 50)
