from person import Person

p1 = Person("Siju", "Abraham", 46)
print(p1)
p1.say_hi()

p2 = Person("Binu", "Varghese", 50)
print(p2)

print(len([1, 2, 3]))
print(len("a string"))
print(len(p1))
print(len(p2))
print(p1.get_fullname())
print(p1.get_first_name())
print(p1.get_last_name())
print(p1.get_age())
print(p1.set_first_name('serene'))
print(p1.set_last_name('varghese'))
print(p1.get_fullname())
print("de" in p1)
