correct_password="admin"
attemps=3
while True:
    password=input("Введите пароль: ")
    if password == correct_password:
        print("Пароль верный")
        break
    else:
        attemps-=1
        if attemps>0:
            print(f"Неверный пароль. Осталось попыток: {attemps}")
        else:
            print("Вход ограничен")
            break