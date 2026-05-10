''' CLASS deep diving
   (1) ENCAPSULATION (ximoya qilish degani)
   (2) IMHERITENCE
   (3) POLIMORPHISM
'''
print("===== ENCAPSULATION =====")
'''
C++ JAVA >  public pribate protected
Phthon > name (public) |  __name(private) | _name(protected). (__) => chiziqlar underline dep ataladi
'''


class Account():
    # state
    description = "the class makes bank account"

    # construction
    def __init__(self, owner, amount):
        self.__owner = owner  # private qilindi ximoya qilindi
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print(f" deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

# getter => yani malumotlarni to'g'ridan to'g'ri olib o'qishimiz mumkun
    @property
    def holder(self):
        return self.__owner
# setter => malumotllarni o'zgartirish®

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


# yangi object
my_account = Account("NEO", 1000)
my_account.get_balance()

print("------------------------------")
my_account.deposit(4500)
my_account.withdraw(500)
my_account.get_balance()

print("================")
try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("no target state fpunt:", err)


# account_owner = my_account.holder  # state
# print("account_owner:", account_owner)
print("owner before:", my_account.holder)  # state
my_account.holder = "ILYOSBEK"  # state
print("owner after:", my_account.holder)
