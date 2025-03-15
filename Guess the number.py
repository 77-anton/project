import random
import time
import sys


# Анімація
def long_loading_animation():
    animation = ["|", "/", "-", "\\"]
    print("Гра завантажується...", end="", flush=True)
    for _ in range(20):
        for symbol in animation:
            time.sleep(0.2)
            print(f"\rГра завантажується... {symbol}", end="", flush=True)
    print("\nГотово!")


# Анімація
long_loading_animation()
print("Вітаю в грі 'Вгадай число!'")

number = random.randint(1, 1000000)

guess = 0

while guess != number:
    guess = int(input("Вгадай число від 1 до 1000000: "))

    if guess < number:
        print("Загадане число більше. Спробуй ще раз!")
    elif guess > number:
        print("Загадане число менше. Спробуй ще раз!")
    else:
        print(f"Вітаю! Ти вгадав число {number}!")