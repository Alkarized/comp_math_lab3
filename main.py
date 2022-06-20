# Вариант - 18
# Методы: Симпсона и трапеций
# ручной интеграл - INT_2^4 (x^3 - 5x^2 + 3x - 16)dx

import numpy as np
from sympy import *


def print_error():
    print("Неправильно введенные данные, попробуйте еще раз")


class Method(object):
    def __init__(self, run, text):
        self.run = run
        self.text = text


class Integral(object):
    def __init__(self, symbol, expression, text):
        self.symbol = symbol
        self.expression = expression
        self.text = text


def get_eps_len(epsilon):
    print(epsilon)
    return len(str(epsilon)) - 2


def trap_it(integral, down, top, n):
    h = (top - down) / n
    x = integral.symbol
    y_0 = integral.expression.subs(x, down)
    y_n = integral.expression.subs(x, top)
    sums = 0
    for i in range(1, n):
        sums += integral.expression.subs(x, down + h * i)
    sums *= 2
    sums += y_0 + y_n
    sums *= h / 2
    return sums


def solve_t(meth, integral, down, top, epsilon):
    lengt = get_eps_len(epsilon)
    print(lengt)
    n = 4
    while True:
        i0 = meth(integral, down, top, n)
        i1 = meth(integral, down, top, 2 * n)
        if abs(i0 - i1) < epsilon:
            print("Полученное значение интеграла:", round(i1, lengt))
            print("Число разбиений:", n)
            break
        else:
            n *= 4


def simp(integral, down, up, n):
    h = (up - down) / n
    x = integral.symbol
    y_0 = integral.expression.subs(x, down)
    y_n = integral.expression.subs(x, up)
    sums = 0
    for i in range(1, n):
        temp = integral.expression.subs(x, down + i * h)
        if i % 2 == 0:
            sums += 2 * temp
        else:
            sums += 4 * temp

    sums += y_0 + y_n
    sums *= h / 3

    return sums


def create_integrals():
    intgs = list()
    x = Symbol("x")
    intgs.append(Integral(x, x ** 2, "x^2"))
    intgs.append(Integral(x, x ** 3 - 5 * x ** 2 + 3 * x - 16, "x^3 - 5x^2 + 3x - 16)"))
    return intgs


# method, integral, left, right, epsilon
def read_all(meths, integs):
    meth = get_method("Выберите метод решения", meths)
    integ_i = get_method("Выберите интеграл", integs)

    while True:
        bot = get_pred("Выберите нижний предел интегрирования: ")
        top = get_pred("Выберите верхний предел интегрирования: ")
        if bot >= top:
            print_error()
        else:
            break

    epsilon = get_epsilon("Введите точность")

    solve_t(meths[meth - 1].run, integs[integ_i - 1], bot, top, epsilon)

    # if bot > top:
    #     bot, top = top, bot
    #     print("Верх стал низом, а низ стал верхом")
    # elif bot == top:
    #     print("Одинаковые пределы интегрирования")
    #     print("Ответ: 0")


def get_method(text, meths):
    print(text)
    for i in range(0, len(meths)):
        print(str(i + 1) + ":", meths[i].text)
    while True:
        try:
            m_i = read_int(None, 1, len(meths) + 1)
            if m_i is None:
                raise ValueError
            return m_i
        except ValueError:
            print_error()


def get_pred(text):
    while True:
        try:
            m_i = float(input(text))
            return m_i
        except ValueError:
            print_error()


def get_epsilon(text):
    while True:
        try:
            m_i = read_float(text, 0, 1)
            if m_i is None:
                raise ValueError
            return m_i
        except ValueError:
            print_error()


def read_float(text, left, right):
    if text is not None:
        print(text, "от", left, "до", right)
    temp = float(input())
    if left <= temp <= right:
        return temp
    else:
        return None


def read_int(text, left, right):
    if text is not None:
        print(text + " от " + left + " до " + right)
    temp = int(input())
    if left <= temp <= right:
        return temp
    else:
        return None


def create_methods():
    temp = list()
    temp.append(Method(trap_it, "Метод трапеций"))
    temp.append(Method(simp, "Метод Симпсона"))
    return temp


if __name__ == '__main__':
    integrals = create_integrals()
    methods = create_methods()
    read_all(methods, integrals)
