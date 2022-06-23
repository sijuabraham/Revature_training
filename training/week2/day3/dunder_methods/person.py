
class Person:

    def __init__(self, fn, ln, a):
        self.__first_name = fn
        self.__last_name = ln
        self.__age = a
        self.__fullname = f"{self.__first_name} {self.__last_name}"

    def __str__(self):
        return f"Person object[first_name = {self.__first_name}, last_name = {self.__last_name},age = {self.__age}]"

    def __len__(self):
        return len(self.__fullname)

    def __contains__(self, name):
        if name in self.__fullname:
            return True

            return False

    def say_hi(self):
        print(f"Hi, my name is {self.__first_name} {self.__last_name} and my age is {self.__age}")

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_fullname(self):
        return self.__fullname

    def set_first_name(self, first_name):
        self.__first_name = first_name
        self.__fullname = f"{self.__first_name} {self.__last_name}"
        return self.__fullname

    def set_last_name(self, last_name):
        self.__last_name = last_name
        self.__fullname = f"{self.__first_name} {self.__last_name}"
        return self.__fullname

    def set_age(self, age):
        self.__age = age
        return self.__age


