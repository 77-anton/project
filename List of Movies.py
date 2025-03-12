movies = []

while True:
    print("\nПрограма 'Список Фільмів'")
    print("1. Додати фільм")
    print("2. Показати всі фільми")
    print("3. Видалити фільм")
    print("4. Вийти")

    choice = input("Виберіть опцію (1-4): ")

    if choice == "1":
        movie = input("Введіть назву фільму: ")
        movies.append(movie)
        print(f"Фільм '{movie}' додано до списку.")

    elif choice == "2":
        if not movies:
            print("Список фільмів порожній.")
        else:
            print("\nСписок фільмів:")
            for i, movie in enumerate(movies, 1):
                print(f"{i}. {movie}")

    elif choice == "3":
        if not movies:
            print("Список фільмів порожній, видаляти нічого.")
        else:
            for i, movie in enumerate(movies, 1):
                print(f"{i}. {movie}")
            try:
                index = int(input("Введіть номер фільму для видалення: "))
                if 1 <= index <= len(movies):
                    deleted_movie = movies.pop(index - 1)
                    print(f"Фільм '{deleted_movie}' видалено зі списку.")
                else:
                    print("Неправильний номер фільму.")
            except ValueError:
                print("Будь ласка, введіть коректний номер.")

    elif choice == "4":
        print("Вихід з програми. До побачення!")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")