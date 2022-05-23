#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import math

"""
С использованием многопоточности для заданного значения найти сумму ряда с точностью члена ряда по абсолютному
значению 1e-07 и произвести сравнение полученной суммы с контрольным значением функции для двух бесконечных
рядов.
"""

CONST_PRECISION = 1e-07


def func_x(x=-0.7):
    result = 1/(math.pow((1 - x), 2))
    return result


def func_y(x=-0.35):
    result = 1/math.log10(math.sqrt((1 + x) / (1 - x)))
    return result


def summ_1(x):
    n, s, m, curr = 0, 0, 0, 0
    while True:
        pre = (n + 1) * x**n
        n += 1
        if abs(curr - pre) < CONST_PRECISION:
            break
        curr = (n + 1) * x**n
        s += curr
    return s


def summ_2(x):
    n, s, curr = 0, 0, 0
    while True:
        second = 2 * n + 1
        first = x ** (2 * n + 1)
        pre = first / second
        n += 1
        if abs(curr - pre) < CONST_PRECISION:
            break
        curr = first / second
        s += curr
    return s


def compare(x, y):
    result = x - y
    print(f"Результат сравнения {result}")


if __name__ == '__main__':
    th1 = Process(target=compare(summ_1(), func_x()))
    th2 = Process(target=compare(summ_2(), func_y()))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
