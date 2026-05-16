''' ARRAY & SET
(1) array
(2) set
(3) specific operators with set
'''

# arrayni ishlatmoqchi bo'lsak array nomlik packcageni ichiga kirib array contructorni qabul qilish kerak

from array import array
print("===== Array =====")
# juda katta xajmdagi sonlar ketma ketligi bo'lsa arraydan foydalanadi kichik xajmda esa listdan
# (i , f ) > intijer
numbers = array("i", [1, 4, 5, 7, 8, 41])
print("number(1)", numbers)


numbers.append(100)
numbers.insert(0, 14)
print("number(2)", numbers)

numbers.remove(5)
numbers.pop()
print("number(3)", numbers)

del numbers[0:2]
print("number(4)", numbers)

print("===== SET =====")
# set > bu unique collection > (takrorlanmaydigon qalleksiya) xisoblanadi yani takroriy sonlarni 1 marotaba qabul qiladi
# setda {gullik qaus chiqadi}
new_numbers = array("i", [1, 7, 5, 4, 4, 5, 7, 4, 8, 41])
numbs_set = set(new_numbers)

print("numbs_set:", numbs_set)
# farmat orqalik print qilsih
print(f"the numbs_set: {numbs_set} and type: {type(numbs_set)}")


# methodlar
numbs_set.add(200)
print("numbs_set(1):", numbs_set)  # 200 yangi son qo'shildi

numbs_set.add(7)
# 7 soni qo'shilmaydi chunki (set)takroriy sonni qo'shmaydi
print("numbs_set(2):", numbs_set)

print("===== specific operators: | & - ^ =====")
# maxsus operatorlar => (| & - ^)

a = {10, 20, 50}
b = {20, 40}

# (|) union ikkala setdagi raqamlarni birga ko'rsatadi va takroriy sonni 1 tasi qabul bo'ladi
natija = a | b
# (&)=> intersection yani ikkkala setda takroriy bo'lgan sonni olib beradi
natija1 = a & b
# (-)=> difference tafout degani ikkalla setdan ayrib jatijani chiqaradi
natija2 = a - b
# (^)=> symetric difference yani ikkala setda takririy bo'lmagan sonlarni chiqarib beradi
natija3 = a ^ b
print("natija:", natija)
print("natija1:", natija1)
print("natija2:", natija2)
print("natija3:", natija3)
