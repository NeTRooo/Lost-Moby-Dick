#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_input():
    return input("Введите значение: ")
def test_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def str_to_int(value):
    return int(value)
def print_int(number):
    print(number)
if __name__ == '__main__':
    user_value = get_input()
    if test_input(user_value):
        int_value = str_to_int(user_value)
        print_int(int_value)
    else:
        print("Введенное значение нельзя преобразовать в целое число.")