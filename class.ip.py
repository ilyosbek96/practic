''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITENCE <
    (3) POLOMORPHISM <

'''

print("======== INHERITENCE ========")
# PARENT(OTA) > CHILD(FARZAND) > parenrt o'ziining pablic va protected propertilarini(state + metdhod)ni childga  daqtim qila oladi


class Animal:  # pythonda qavush qo'yish shartmas chunki automat qo'yib beradi
    # state
    description = "the class create animals"
    # construction

    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # CHILD
    # STATE

    # CONSTRUCTION perentdan properti qabul qilib oladi
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # METHOD
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("yes, i can protect you!")


class Cat(Animal):  # CHILD
    # STATE

    # CONSTRUCTION perentdan properti qabul qilib oladi
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # METHOD
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # CHILD
    # STATE

    # CONSTRUCTION perentdan properti qabul qilib oladi
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # METHOD
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("yes, i can swim!")


dog = Dog("REX", "wow", True)
cat = Cat("TOM", "myeow", True)
fish = Fish("NOME", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("===============")
dog.make_voice()
cat.make_voice()
fish.make_voice()

print(dog.voice, fish.voice)
print("dog.status;", dog.status)
print("cat.status;", cat.status)
