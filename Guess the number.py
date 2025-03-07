import random

# Генеруємо випадкове число від 1 до 10
secret_number = random.randint(1, 10)

print("Вгадай число від 1 до 10!")

while True:
    try:
        # Користувач вводить число
        guess = int(input("Введи своє число: "))

        # Перевіряємо, чи вгадав користувач
        if guess == secret_number:
            print("Вітаю! Ти вгадав число!")
            break
        elif guess < secret_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")

    except ValueError:
        # Обробка випадку, якщо користувач ввів не число
        print("Будь ласка, введіть ціле число.")

print("Гра закінчена.")