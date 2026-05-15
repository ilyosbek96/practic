''' TUPLE
(1) TUPLE  o'zi nima: typle va list
(2)
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
