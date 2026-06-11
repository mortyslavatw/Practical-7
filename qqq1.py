print("Проверка рейтинга продукта")

rating=int(input("Введите рейтинг продукта: "))

match rating:
    case 1|2|3:
        result= "Плохой продукт"
        emoji= "❌"
        recommendations="Не рекомендую пробовать"
    case 4|5|6:
        result= "Средний продукт"
        emoji= "🙂"
        recommendations="Можно попробовать"
    case 7|8|9:
        result="Хороший продукт"
        emoji="😁"
        recommendations="Хороший выбор"
    case 10:
        result="Отличный продукт"
        emoji="👍"
        recommendations="Прекрасный выбор"
    case _:
        result="Введен некорректный рейтинг продукта"
        emoji="❗"
        recommendations=""
        print("Введите корректный рейтинг продукта в пределах от 1 до 10")
print(f"Рейтинг продукта: {result}")
print(f"Эмодзи: {emoji}")
print(f"Рекомендации к продукту: {recommendations}")
