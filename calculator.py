for _ in range(100):  # Великий запас ітерацій, щоб користувач міг кілька разів виконати обчислення
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть оператор (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ділення на нуль неможливе!")
            continue
    else:
        print("Невідомий оператор!")
        continue

    print(f"Результат: {result}")

    choice = input("Бажаєте продовжити? (так/ні): ").strip().lower()
    if choice == 'ні':
        print("Калькулятор завершив роботу.")
        break  # Вихід із циклу, якщо користувач вводить "ні"
