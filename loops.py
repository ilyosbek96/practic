'''  LOOP operatorlari
(1) for
(2) break/else
(3) while
'''
# Iterable>(takrorlash -aylantirish ) object > string dict tuple list range map filter
# string > String (matn) → Har bir belgisi bo‘yicha iteratsiya qilinadi.
# dict > Dict (lug‘at) → Kalitlari bo‘yicha iteratsiya qilinadi.
# tuple > Tuple (kortej) → Listga o‘xshash, lekin o‘zgarmas.
# range > Range → Ketma-ket sonlar generatori.
# map > Map → Funksiyani har bir elementga qo‘llab, yangi iterable (takrorlash -aylantirish ) hosil qiladi.
# filter > Filter → Shartga mos elementlarni tanlab oladi.

print("=====  for operatorlari =====")
# for ketma ketlikda degani
text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="m5cs", ear=2025)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

print("="*15)
for number in numbs:
    print(f"the number: {number}")
print("="*15)
for x in range_obj:
    print(f"the element: {x}")
print("="*15)
for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")

print("="*15)
for x in range(1, 20, 5):  # step yani 1 +5 xar natijaga 5 + ketiladi
    print(f"the x: {x}")

print("=====  break/else =====")
for l in range(1, 8):
    print(f"the l: {l}")
    if l > 6:  # 8dan yuqori bo'lsa (amalga oshdi chiqadi)
        print("to'xtatildi")
        break
else:
    print("amalga oshdi")

# while takrorlanishning miqdori anq bo'lmagan xollarda while ishlatiladi
print("=====  while operatorlari =====")
numb = 40
while numb > 0:
    numb -= 10
    print(f"the numb {numb}")

print("="*15)
count = 0
while True:
    count += 1
    x = int(input("raqam kiriting "))  # int degani intijer degani

    if x == 41:
        print(f"siz raqamni {count} urunishda toptingiz")
        break  # toxtatiladi degani
    else:
        print("qaytadan raqam kiriting")
