#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def circle(radius):
    return math.pi * radius ** 2
def cylinder():
    radius = float(input('Введите радиус цилиндра: '))
    height = float(input('Введите высоту цилиндра: '))
    side_area = 2 * math.pi * radius * height
    full_area = side_area + 2 * circle(radius)
    choice = input('Хотите получить только боковую площадь? (да/нет): ').lower()
    if choice == 'да':
        return side_area
    elif choice == 'нет':
        return full_area
    else:
        return 'Неправильный выбор.'
if __name__ == '__main__':
    result = cylinder()
    print(f'Площадь цилиндра: {result}')