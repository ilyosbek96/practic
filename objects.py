'''OBJECTS 
(1) WHAT is object
(2) Iterable objects & RANGE 
(3) DICTIONARY
(4) ERROR handling system
'''

import array  # package/module
# bironbir packageni yaxlit object qilib chaqirmoqchi bo'lganda (import deb package nomi yoziladi)
import math   # package
# from orqalikxam chaqirib olish mumkun
# anq bir state yoki method chaqirilayotganda esa from orqalik math (package) ceil (methodini) qo'lga olish o'li
from math import ceil
print("===== what is object =====")
# OBJECT o'zining state va methodiga ega bo'lgan maxsus data type
# PYTHONda xamma narsa OBJECT

print(type("hello world"))  # type bu function
print(type(100))       # type bu function
print(type(True))       # type bu function
print(type(array))       # type bu function
print(type(math))         # type bu function

# PARADIGMA BU USLUBIYAT DEGANI => eng mashhurlari OBJECT-ORIENTED PROGRAMMING (OOP > OBYEQTLARGA ASOSLANGAN DASTURLASH)
# OOP > CONCEPTSIYALARI 4 TA > ABSTRACTION | ENCAPSULATION | INHERITENCE | POLIMORPHISM
#  FUNCTIONAL PROGRAMMIMG
# CALL CAIL => methodining define qismi bu MATH package ni ichida hisoblanadi
# CALL MATH ESA OBJECT CEIL ESA BU METHOD HHISOBLANADI
natija = math.ceil(97.7)
print("natija", natija)

natija1 = ceil(98.7)
print("natija1", natija1)
