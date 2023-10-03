try:
    num1=int(input("Введите число 1:"))  
    num2=int(input("Введите число 2:"))  
    print("Поделим числа:",num1/num2)   
except ValueError:
    print("Неудачное преобразование")   
except ZeroDivisionError:
    print("Нельзя делить на ноль")  
except Exception:
    print("Исключение") 
finally:
    print("Пока!!")