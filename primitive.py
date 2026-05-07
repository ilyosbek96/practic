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
