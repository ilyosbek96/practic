''' Packages & Debugging
   (1) PYTHON PACKAGE & CORE PACKAGE
   (2) PACKAGE MANAGER & EXTERNAL PACKAGE
   (3) DEBUGGING
'''
import turtle
print("===== PYTHON PACKAGE & CORE PACKAGE =====")
''' Python Package/ Modulelari: Core, File, External  '''
""" CORE PACKAGE > pyrhon bilan yonmayon yurodigon package xisoblanadi """
''' CORE PACKAGE => LINKI > https://docs.python.org/3/library'''
# import orqalik ulanadi

# Core
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.circle(100)

turtle.done()

print("="*15)
# fileni ulash
# open orqalik filelarni o'chish mumkun
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)  # file ochilyapti
finally:
    my_file.close()  # file yopilyapti (albatta fileni yopib qo'yish kerak)

# oddiy qilib yozish uchun {with} orqalik qilsaxam bo'ladi
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    # wiht filechi ochib ishga tushgandan kegin o'zi close  yani yopib qoyadi
    print("your_content:",  your_content)
