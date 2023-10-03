def check(val):
        if isinstance(val, dict):
            print("Словарь")
            sort = sorted(val, key=val.get)
            small = sort[:3]
            return {key: val[key] for key in small}
        elif isinstance(val, list):
            print("Список")
            zeroo = [x for x in val if x != 0]
            if len(zeroo) >= 2:
                positive = [x for x in zeroo if x > 0]
                if len(positive) >= 2:
                    itog = positive[0] * positive[1]
                    return itog
        elif isinstance(val, int):
            print("Число")
            st_val = str(val)
            count = len(st_val)
            print(f"В числе {count} разрядов")
        elif isinstance(val, str):
            print("Строка")
            k = set(val)
            new = dict.fromkeys(k, 0)
            for k in val:
                new[k] += 1
            print(new)
        else:
            print("Тип аргумента не поддерживается")

while True:
    print("Выберите тип данных:")
    print("1. Словарь")
    print("2. Список")
    print("3. Число")
    print("4. Строка")
    print("5. Выход")
    ch = input("Введите номер:")
    if ch == "1":
        rez = {'a': 5, 'b': 2, 'c': 10, 'd': 3}
        check(rez)
    elif ch == "2":
        print(check([0, 2, 4, 6, 8, -3, -5]))
    elif ch == "3":
        try:
            input_val = input("Введите число: ")
            rez = int(input_val)
            check(rez)
        except ValueError:
            print("Введите корректное число!")
    elif ch == "4":
        input_val = input("Введите строку: ")
        check(input_val)
    elif ch == "5":
        print("До свидания!")
        break
    else:
        print("Неверный выбор!")