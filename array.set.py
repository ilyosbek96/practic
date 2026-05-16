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

# methodlar
numbers.append(100)
numbers.insert(0, 14)
print("number(2)", numbers)

numbers.remove(5)
numbers.pop()
print("number(3)", numbers)

del numbers[0:2]
print("number(4)", numbers)
