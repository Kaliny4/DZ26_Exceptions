"""
Создать программу-калькулятор в виде класса и несколько методов,
как минимум сложение, вычитание, деление, умножение, возведение в степень
и извлечение квадратного корня.
Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений,
как минимум деление на 0.
Создать своё исключение, к примеру возведение в отрицательную степень.
"""
import math


class New_exept(Exception):
    pass


class Calc(object):
    first_num = 0
    second_num = 0

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        try:
            result = self.first_num + self.second_num
        except TypeError:
            print('check input')
            result = 0
        except Exception:
            print('Error')
            result = 0
        return result

    def subs(self):
        try:
            result = self.first_num - self.second_num
        except TypeError:
            print('check input')
            result = 0
        except Exception:
            print('Error')
            result = 0
        return result

    def mult(self):
        try:
            result = self.first_num * self.second_num
        except TypeError:
            print('check input')
            result = 0
        except Exception:
            print('Error')
            result = 0
        return result

    def div(self):
        try:
            result = self.first_num / self.second_num
        except ZeroDivisionError as err:
            print(f'second_num is zero {err}!!!')
            result = None
        except TypeError:
            print('check input')
            result = 0
        except Exception:
            print('Error')
            result = 0
        return result

    def exp(self):
        try:
            result = self.first_num ** self.second_num
            if self.second_num < 0:
                raise New_exept
        except New_exept:
            print('second_num is a minus number!!!')
            result = None
        except TypeError:
            print('check input')
            result = 0
        except Exception:
            print('Error')
            result = 0
        return result

    def sqrr(self):
        try:
            a = math.sqrt(self.first_num)
            if self.second_num < 0:
                raise New_exept
            b = math.sqrt(self.second_num)
            result = (f'Square root of the first number: {a}; '
                      f'Square root of the second number: {b}')
        except New_exept:
            print('second_num is a minus number!!!')
            result = None
        except TypeError:
            print('check input')
            result = 0
        except Exception:
            print('Error')
            result = 0
        return result


try:
    c = Calc(int(input('Enter first number: '))
             , int(input('Enter second number: ')))
    print(f'Addition: {c.add()}')
    print(f'Subtraction: {c.subs()}')
    print(f'Multiplication: {c.mult()}')
    print(f'Division: {c.div()}')
    print(f'Exponention: {c.exp()}')
    print(f'Square root: {c.sqrr()}')
except ValueError:
    print('ValueError, check input')













