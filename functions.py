import animals
import os
# Создаем объекты Birds
goose_s = animals.Birds('Гусь', 'Серый', 'кря-кря', 10, 15)
goose_w = animals.Birds('Гусь', 'Белый', 'кря-кря', 9, 8)
chicken_ko = animals.Birds('Курица', 'Ко-ко', 'КУКАРЕКУУУ', 10, 15 )
chicken_ky = animals.Birds('Курица', 'Ку-ка-реку', 'КУКАРЕКУУУ', 8, 11 )
duck = animals.Birds('Утка','Кряква','кря-кря-кря', 7, 0)

# Создаем объекты Cattle
cow = animals.Cattle('Корова', 'Манька', 'Муууу', 135, 30)
goat_r = animals.Cattle('Коза', 'Рога', 'Бее-бее', 80, 12)
goat_k = animals.Cattle('Коза', 'Копыта', 'Бее-бее', 90, 18)

# Создаем объекты Sheep
sheep_b = animals.Sheep('Овца', 'Барашек', 'Беее', 37, 20)
sheep_k = animals.Sheep('Овца', 'Кудрявый', 'Беее', 46, 15)

# Функция начала
def start():
    print('ЖИВОТНЫЕ НА ФЕРМЕ ДЯДИ ДЖО')
    print('===========================')
    print(f'На ферме дяди Джо бегают животные:')
    # Птицы
    print(f'\nПтички: ')
    print(f'{goose_s.get_type()}, которого зовут {goose_s.get_name()}')
    print(f'{goose_w.get_type()}, которого зовут {goose_w.get_name()}')
    print(f'{chicken_ko.get_type()}, которого зовут {chicken_ko.get_name()}')
    print(f'{chicken_ky.get_type()}, которого зовут {chicken_ky.get_name()}')
    print(f'{duck.get_type()}, которого зовут {duck.get_name()}')
    # Рогатый скот
    print(f'\nКрупный рогатый скот: ')
    print(f'{cow.get_type()}, которую зовут {cow.get_name()}')
    print(f'{goat_r.get_type()}, которую зовут {goat_r.get_name()}')
    print(f'{goat_k.get_type()}, которую зовут {goat_k.get_name()}')
    # Овцы
    print(f'\nОвцы: ')
    print(f'{sheep_b.get_type()}, которую зовут {sheep_b.get_name()}')
    print(f'{sheep_k.get_type()}, которую зовут {sheep_k.get_name()}')

# Функция работы на ферме
def work():
    # Начинаем работать на ферме
    print(f'\nДядя джо уже старый и ему нужна ваша помощь.')
    print(f'Помогите ему подоить коров и коз, собрать яйца у птиц и подстричь овец.')
    ready = input('Вы готовы начать помогать дяде Джо? : y/n ')
    action = False
    while action == False:
        if ready == 'y':
            os. system('CLS')
            action = True
        else:
            ready = input('Вы готовы начать помогать дяде Джо? : y/n ')

    # Собираем яйца
    print('Начнем с простого, соберем яички у птиц.')
    print(f'{goose_s.get_type()}, которого зовут {goose_s.get_name()} снес \
    {goose_s.get_eggs()} яиц')
    take_eggs = input('Введите число яиц которое нужно забрать: ')
    action = False
    while action == False:
        if int(take_eggs) == goose_s.get_eggs():
            goose_s.set_eggs(take_eggs)
            print('Молодец!')
            print(f'У {goose_s.get_type()}, которого зовут {goose_s.get_name()}\
            осталось {goose_s.get_eggs()} яиц')
            action = True
        else:
            print('Не правильно!')
            take_eggs = input('Введите число яиц которое нужно забрать: ')

    # Доим корову
    print('\nТеперь подоим корову!')
    print(f'{cow.get_type()}, которую зовут {cow.get_name()} давно не доили\
    предположительно у нее накопилось {cow.get_milk()} литров молока.')
    take_milk = input('Подоить корову? y/n ')
    action = False
    while action == False:
        if take_milk == 'y':
            print('Молодец!')
            cow.set_milk(1)
            print(f'У {cow.get_type()}, которую зовут {cow.get_name()}\
            осталось {cow.get_milk()} молока')
            action = True
        else:
            print('Не правильно!')
            take_milk = input('Подоить корову? y/n ')

    # Стрижем шерсть овцы
    print('\nПоследнее задание, подстричь овцу!')
    print(f'{sheep_b.get_type()}, которую зовут {sheep_b.get_name()} давно \
    не стригли предположительно у нее накопилось {sheep_b.get_wool()} \
    сантиметров шерсти')
    take_wool = input('сколько сантиметров шерсти нужно состричь? : ')
    action = False
    while action == False:
        if int(take_wool) == sheep_b.get_wool():
            print('Молодец!')
            sheep_b.set_wool(take_wool)
            print(f'У {sheep_b.get_type()}, которую зовут {sheep_b.get_name()}\
            осталось {sheep_b.get_wool()} сантиметров шерсти')
            action = True
        else:
            print('Не правильно!')
            take_wool = input('сколько сантиметров шерсти нужно состричь? : ')

    # Последнее задание
    print('\nОтлично! Вы помогли дяде Джо с делами на ферме.')
    last_step = input('Ну что двигаемся дальше? : y/n  ')
    action = False
    while action == False:
        if last_step == 'y':
            os. system('CLS')
            action = True
        else:
            last_step = input('Ну что двигаемся дальше? : y/n  ')

def end():
    print('Теперь по последнему заданию мы должны выяснить общий вес всех животных.')
    print('А так же самого тяжелого зверя на ферме.')
    print(f'\nОбщий вес равен: ', (goose_s.get_weight() + goose_w.get_weight() + \
    chicken_ko.get_weight() + chicken_ko.get_weight() + duck.get_weight() + \
    cow.get_weight() + goat_r.get_weight() + goat_k.get_weight() + \
    sheep_b.get_weight() + sheep_k.get_weight()),' килограмм')

    print('Максимальный вес одного зверя: ', max(goose_s.get_weight() , goose_w.get_weight() , \
    chicken_ko.get_weight() , chicken_ko.get_weight() , duck.get_weight() , \
    cow.get_weight() , goat_r.get_weight() , goat_k.get_weight() , \
    sheep_b.get_weight() , sheep_k.get_weight()), ' килограмм')
    print(f'И зверь этот: {cow.get_type()} {cow.get_name()}')
