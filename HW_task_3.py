"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

from itertools import combinations as comb

goods = {'палатка': 2.0,
         'спальный мешок': 1,
         'фонарь': 0.4,
         'спички': 0.03,
         'кружка': 0.1,
         'фляжка': 0.3,
         'куртка': 0.9,
         'нож': 0.2,
         'ложка': 0.1,
         'миска': 0.1,
         'коврик': 0.3,
         'котелок': 2.6,
         'топор': 1.5,
         'тапочки': 0.35,
         'веревка': 1.2,
         'дождевик': 0.1,
         'сапоги': 1.3,
         'аптечка': 0.7,
         'консервы': 1.75,
         'компас': 0.05,
         'батарейки': 0.4,
         'крупы': 2,
         'мыло': 0.2
         }
counter = 1
weight = float(input('Введите максимальную грузоподъёмность рюкзака: '))
for count in range(1, len(goods)):
    for item in comb(goods, count):
        my_list = {}
        for obj in item:
            my_list[obj] = goods[obj]
        if sum(my_list.values()) <= weight:
            print(f'Вариант {counter}: {my_list.keys()}')
            counter += 1
