# Наследование


# родительский класс


class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# дочерний класс
class Penguin(Bird):

    def __init__(self):
        # вызов функции super()
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


# Инкапсуляция


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# изменяем цену
c.__maxprice = 1000
c.sell()

# используем функцию сеттера
c.setMaxPrice(1000)
c.sell()


# Полиформизм


class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# общий интерфейс
def flying_test(bird):
    bird.fly()


# создаем объекты
blu = Parrot()
peggy = Penguin()

# передаем объекты
flying_test(blu)
flying_test(peggy)


# Абстракция


class Animal:

    def __init__(self, name):
        self.name = name

    def makeNoise(self):
        pass


class Dog(Animal):

    def makeNoise(self):
        print(self.name + " says: Woof!")


class Cat(Animal):

    def makeNoise(self):
        print(self.name + " says: Meow!")


dog = Dog("Baxter")
cat = Cat("Oliver")
dog.makeNoise()
cat.makeNoise()
