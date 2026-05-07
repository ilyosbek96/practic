print("====== number =======")
# JAVAda ,varible bu malumot manzilining nomlanish
# PYTHON, variable bu lar reference nomlanishi

count = 100
count_type = type(count)  # class intdan olingan insilt xisoblanadi
print("count", count, count_type)
# printni qisqa qilib bu farmat string orqalikyozish gullik qausdan foydalanilkadi
print(f"the count: {count} va type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print("====== string =======")
# SRTRINGxam primitiv variable xisoblanadi lekn buxam o'ziniing method va statelariga ega xisoblanadi
# STRING METHODLARI: upper() lower() title() find() replace()


course = "AI Python FullStack"
result = type(course)
print(f"Yangi result (1): {result}")
result = course.title()
print(f"Yangi result (2): {result}")

# .           METHODNI tekshirish yo'li variable omi va . nuqta bosilsa methodlar chiqadi

# UPPPER Mmethod string dagi xarflarni katta xarifga o'zgartirib beradi
result = course.upper()
print(f"Yangi result (3): {result}")

# REPLACE almashtirishda ishlatiladi
result = course.replace("FullStack", "MasterClass")
print(f"replace: {result}")

print("====== boolean =======")
# function > input() tpe() bool() int() str()
y = input('give your value for y:')
print("y:", y)

# booleanga boglash
result = y.isnumeric()  # ISNUMERIC son kiritilsa true xarf kritilsa false qaytaradi
print(f"isnumeric: {result}")

#           TRUTHY VA FALSY VALUELAR
# TRUTHY > TRUE 100 -100 "ilyosbek"
# FALSY > FALSE 0 "" none
# FALSY QIYMATLARI AGAR ORASIDA RU QIYMAT BOLSA TRUE QAYTARADI (100)>true qiymat
test_falsy = "" or False or None or 0 or 100
print("the FALSY:", bool(test_falsy))

# FALSY > FALSE 0 "" none
test_true = "MIT"
print("the TRUE:", bool(test_true))
