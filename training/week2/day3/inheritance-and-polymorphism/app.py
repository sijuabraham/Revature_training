class Animal:

    def __init__(self, color, number_of_eyes):
        self.__color = color
        self.__number_of_eyes = number_of_eyes

    def make_noise(self):
        print("**GENERIC ANIMAL NOISE**")


class Dog(Animal):

    def __init__(self, name, color, number_of_eyes):
        super().__init__(color, number_of_eyes)
        self.name = name

    def play_game(self):
        print(f"{self.name} is playing fetch!")

    def make_noise(self):
        print(f"{self.name} says bark!")


d1 = Dog("Fido", "Black", 2)
d2 = Dog("Sparky", "Brown", 2)
d1.play_game()
d2.play_game()
print(d1.name)
print(d2.name)
d1.make_noise()
d2.make_noise()
