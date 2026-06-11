num1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

match operation:
    case '+':
        result = num1 + num2
        print(f"{num1} {operation} {num2} = {result}")
    case '-':
        result = num1 - num2
        print(f"{num1} {operation} {num2} = {result}")
    case '*':
        result = num1 * num2
        print(f"{num1} {operation} {num2} = {result}")
    case '/':
        if num2 == 0:
            print("Ошибка: деление на ноль")
        else:
            result = num1 / num2
            print(f"{num1} {operation} {num2} = {result}")
    case _:
        print("Неизвестная операция")