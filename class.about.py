''' CLASS
    (1) class nima
    (2) oridinary vs static properties (oddiy xususiyatlar vs static xususiyatlar)
    (3) special/magic medhods (maxsus methodlar)
'''
# ======================= METHODlar DUNDER orqalik belgelanadi ==================
print("==== class o'zi nima =====")
# classlar > bu object yasovchi shablon
# classlar strukturalari > state | constructor | method


class Person():
    # state
    mesage = " STATIC state property"
    # constructor

    def __init__(self, name, age):  # self bu object (init > maxsus methhod)
        self.name = name  # self => this degani
        self.age = age

    # method oddiy
    def tanishtiruv(self):  # def defineshin
        print(f"{self.name} says: how do you di!")

    def yosh(self):
        print(f"{self.name} says i am {self.age}")

    # static method @classmethod > orqalik ishlatiladi
    @classmethod  # diqared xisoblanadi
    def explain(cls):
        print("static method property executed")


# YANGI OBJECT
person_obj = Person("Neo", 29)
person_obj1 = Person("MESSI", 29)
person_obj2 = Person("SAS", 29)

# ORDINARY (ODDIY) STATE PROPERTY
# name = person_obj.name
print("person_obj.name:", person_obj.name)

# ordinary method
person_obj.tanishtiruv()
person_obj1.yosh()

print("==== oridinary vs static properties =====")
# static > (classni o'zi bilan birga kelodigon) state
new_message = Person.mesage
print("new_message;", new_message)

# static method isha tushurish uchun object bilan emas class nomi orqalik ishga tushuriladi
Person.explain()

print("====  special/magic medhods (maxsus methodlar) =====")
# PYTHONning eng kop ishlatiladigon maxsus methodlari
# __del__ | __init__ | __new__ | __str__ | __call__ | __getitem__ | (__eq__taqqoshlaganda degani) | __len__ ...
# __init__ Ob’ekt yaratilganda chaqiladi. Konstruktor vazifasini bajaradi.
# __del__ Ob’ekt o‘chirilganda chaqiladi. Destructor sifatida ishlaydi.
# __str__ print() yoki str() chaqirilganda ob’ektni matn ko‘rinishida qaytaradi.
# __len__ len(obj) chaqirilganda ob’ekt uzunligini qaytaradi.
# __getitem__ obj[key] chaqirilganda elementni olishni boshqaradi.
# __call__ Ob’ektni funksiya kabi chaqirish imkonini beradi.
# __eq__, __lt__, __gt__ Tenglik va solishtirish operatorlarini (==, <, >) boshqaradi
# __new__ Python’da __new__ ham magic method hisoblanadi. U obyekt yaratilishidan oldin chaqiladi va aslida obyektni yaratish uchun javobgar
# __new__ klassning yangi instansiyasini yaratadi.Har doim klassni argument sifatida qabul qiladi (cls).Odatda __init__ bilan birga ishlatiladi:__new__ → obyektni yaratadi.__init__ → obyektni sozlaydi (atributlarni to‘ldiradi).Agar __new__ obyekt qaytarmasa, __init__ chaqilmaydi.


class Car():
    # state
    description = "this class makes cars"

    # constructor
    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the {self.name} started engine")

    def stop_engine(self):
        print(f"the {self.name} stopped engine")

    def __str__(self):
        return f"moshinaniing nomi: {self.name} yili {self.year} yil"

# objecni function orqalik chaqirishda __call__ ishlatiladi
    def __call__(self):
        print("objectimiz function kabi chaqirildi")
        return True


my_car = Car("FERRARY", 2025)
my_car.start_engine()
my_car.stop_engine()

# object
print("------")
your_car = Car("tayota", 2026)
print(your_car)
your_car()    # funtionlar kabi orqalik chaqirish
resposse = your_car()
print("return qaytarish:", resposse)
