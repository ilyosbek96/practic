''' Packages & Debugging
   (1) PYTHON PACKAGE & CORE PACKAGE
   (2) PACKAGE MANAGER & EXTERNAL PACKAGE
   (3) DEBUGGING
'''
from PIL import Image
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

# turtle.done()

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

print("===== PACKAGE MANAGER & EXTERNAL PACKAGE =====")
''' PACKAGE MANAGERlar o'rnatish usullari
     Python > pip, pipenv
     NodeJS > npm, yarn
     PHP > compores
     MacOS > brew
'''
# EXTERNAL PACKAGE > link => https://pypi.org
# PACKAGE MANAGER (PIP) pillow rasm chizishga yordam berodigon package o'rnatish mumkun

with Image.open("material/logo.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")
# pip3 list pipni listni ko'rsatadi
# pip3 show pillow desa qayerga ornatilganini bilsih uchun
# cd dep shu linkgborsak /Users/ilyosbek96/Library/Python/3.9/lib/python/site-packages qanday saqlanganini ko'rsa bo'ladi va ls dep ro'yxatni ko'rsa bo'ladi

print("========== DEBUGGING ==========")
# DEBUGGING oqali xatoni toposa bo'ladi


def get_summary(*args):  # define qismi
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount


test = 100
natija = get_summary(1, 2, 3, 4, 5)  # call qismi
print("natija:", natija)
