''' CLASS
    (1) class nima
    (2) oridinary vs static properties (oddiy xususiyatlar vs static xususiyatlar)
    (3) special medhods (maxsus methodlar)
'''
print("==== class o'zi nima =====")
# classlar > bu object yasovchi shablon
# classlar strukturalari > state | constructor | method


class Person():
    # state
    mesage = " STATIC state property"
    # constructor

    def __init__(self, name, age):  # self bu object (init > maxsus methhod)
        self.name = name
        self.age = age

    # method oddiy
    def tanishtiruv(self):  # def defineshin
        print(f"{self.name} says: how do you di!")

    def yosh(self):
        print(f"{self.name} says i am {self.age}")

    # static method @classmethod > orqalik ishlatiladi
    @classmethod
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
