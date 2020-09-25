# Класс животные
class Animals:
    # Инициализируем атрибуты
    def __init__(self):
        self.type_data = []
        self.name_data = []
        self.weight_data = []
        # Добавляем информацию о животных
    def add_specifications(self, animal):
        self.type_data.append(animal.type)
        self.name_data.append(animal.name)
        self.weight_data.append(animal.weight)
        # Выводим информацию о животных
    def get_specifications(self):
        return self.type_data, self.name_data, self.weight_data
        # Считаем общий вес животных
    def calculate_weight(self):
        result = 0
        for animal in self.weight_data:
            result += animal
        return result
        # Получаем самый большой вес
    def get_max_weight(self):
        return max(self.weight_data)
        # Выводим имя животного с самым большим весом
    def info_max_weight_animal(self):
        for id, i in enumerate(self.weight_data):
            if i == max(self.weight_data):
                return self.name_data[id]
# Класс птица
class Bird():
    # Инициализируем атрибуты
    def __init__(self, type, name, weight):
        self.type = type
        self.name = name
        self.weight = weight
        # Метод - покушать
    def set_eat(self, food):
        self.weight += food
        # Собираем яйца
    def get_eggs(self):
        return print('eggs collected')
# Класс Крупного рогатого скота
class Cattle():
    # Инициализируем атрибуты
    def __init__(self, type, name, weight):
        self.type = type
        self.name = name
        self.weight = weight
        # Метод - покушать
    def set_eat(self, food):
        self.weight += food
        # Доим
    def get_milk(self):
        return print('milk collected')
# Класс овца
class Sheep():
    # Инициализируем атрибуты
    def __init__(self, type, name, weight):
        self.type = type
        self.name = name
        self.weight = weight
        # Метод - покушать
    def set_eat(self, food):
        self.weight += food
        # Стрижем
    def get_wool(self):
        return print('wool collected')


# Создаем объект на основе класс птицы
duck = Bird('Утра', 'Кря', 12)
# Собираем и кормим
duck.get_eggs()
duck.set_eat(1)

# Создаем объект на основе класса рогатых
cow = Cattle('Корова', 'Буренка', 79)
# Собираем и кормим
cow.get_milk()
cow.set_eat(5)

# Создаем объект на основе класса овец
ram = Sheep('Баран', 'Кучерявый', 37)
# Собираем и кормим
ram.get_wool()
ram.set_eat(8)

# Создаем объект на основе класса животных
farm_animals = Animals()
# Добавляем информацию о животных
farm_animals.add_specifications(duck)
farm_animals.add_specifications(cow)
farm_animals.add_specifications(ram)

# Выводим информацию о животных
print(farm_animals.get_specifications())
# Считаем общий вес
print(farm_animals.calculate_weight())
# Получаем самый большой вес
print(farm_animals.get_max_weight())
# Получаем имя животного с самым большим весом
print(farm_animals.info_max_weight_animal())
