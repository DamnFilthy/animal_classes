# класс Животные содержит общие сведения обо всех животных
class Animal:
    def __init__(self, type, name, voice, weight):
        self.__type = type
        self.__name = name
        self.__voice = voice
        self.__weight = weight

        # Методы модификаторы
    def set_type(self, type):
        self.__type = type
    def set_name(self, name):
        self.__name = name
    def set_voice(self, voice):
        self.__voice = voice
    def set_weigth(self, weight):
        self.__weight = weight

        # Методы получатели
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_voice(self):
        return self.__voice
    def get_weight(self):
        return self.__weight

class Birds(Animal):
    def __init__(self, type, name, voice, weight, eggs):
        Animal.__init__(self, type, name, voice, weight)
        self.__eggs = eggs

    def set_eggs(self, eggs):
        self.__eggs = int(eggs) - int(eggs)

    def get_eggs(self):
        return self.__eggs

class Cattle(Animal):
    def __init__(self, type, name, voice, weight, milk):
        Animal.__init__(self, type, name, voice, weight)
        self.__milk = milk

    def set_milk(self, milk):
        self.__milk = int(milk) - int(milk)

    def get_milk(self):
        return self.__milk

class Sheep(Animal):
    def __init__(self, type, name, voice, weight, wool):
        Animal.__init__(self, type, name, voice, weight)
        self.__wool = wool

    def set_wool(self, wool):
        self.__wool = int(wool) - int(wool)

    def get_wool(self):
        return self.__wool
