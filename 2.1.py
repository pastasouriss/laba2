import math

def find_nod(m, n):
    return math.gcd(m, n)

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(find_nod(a, b))
except ValueError:
    print("Ошибка! Введите целое число.")
finally:
    print("До свидания!")
