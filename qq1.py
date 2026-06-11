print("=======Определение сезона=======")

month=int(input("Введите номер месяца:"))

match month:
    case 12 | 1 | 2:
            season = "Зима"
            emoji = "❄️"
    case 3 | 4 | 5:
            season = "Весна"
    case 6 | 7 | 8:
            season = "Лето"
            emoji = "☀️"
    case 9 | 10 | 11:
            season = "Осень"
            emoji = "🍂"
    case _:
        print("Введите правильный номер месяца")

print(f"Время года: {season}")
print(f"Эмодзи: {emoji}")
