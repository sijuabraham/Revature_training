class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hi(self):
        print(f"Hi, my name is {self.first_name} {self.last_name}, and Iam {self.age} years old")

    def have_birthday_party(self):
        print("Hooray my birthday is today")


p1 = Person("Siju", "Abraham", 46)
p2 = Person("Binu", "Varghese", 50)
p3 = Person("Chris", "Varghese", 16)
p4 = Person("Serene", "Varghese", 10)
print(p1.first_name)
print(p2.first_name)
print(p3.first_name)
print(p4.first_name)

print(p1.last_name)
print(p2.last_name)
print(p3.last_name)
print(p4.last_name)

print(p1.age)
print(p2.age)
print(p3.age)
print(p4.age)

(p1.say_hi()) # if return is given in the function, then output shows none after the function is executed. Since there
             #   is no return in the function, no need to give print
(p2.say_hi())
(p3.say_hi())
(p4.say_hi())


(p1.have_birthday_party())
Person.say_hi(p1)
print(p1)


class Todo:
    def __init__(self,description):
        self.description = description
        self.completed = False


class User:
    def __init__(self, username, mobile):
        self.username = username
        self.mobile = mobile
        self.todos = []


user1 = User("Siju", "234-234-2342")
todo1 = Todo("Sweep floor")
print(user1.username)
print(user1.mobile)
print(todo1.description)
print(todo1.completed)
print(user1.todos)





