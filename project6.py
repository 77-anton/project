print("Привіт! Ласкаво просимо до гри вікторини")
print("Тобі потрібно правильно відповісти на кілька запитань.")

score = 0  # Лічильник правильних відповідей

# Перше запитання
answer1 = input("Яка столиця України? ")
if answer1.lower() == "київ":
    print("Правильно!!!")
    score += 1
else:
    print("Неправильно! Правильна відповідь: Київ")

# Друге запитання
answer2 = input("Скільки континентів на Землі? ")
if answer2 == "7":
    print("Правильно!!!")
    score += 1
else:
    print("Неправильно! Правильна відповідь: 7")

# Третє запитання
answer3 = input("Яка найбільша планета Сонячної системи? ")
if answer3.lower() == "юпітер":
    print("Правильно!!!")
    score += 1
else:
    print("Неправильно! Правильна відповідь: Юпітер")

# Завершення гри
print(f"Гра завершена! Ти набрав {score} з 3 балів.")
