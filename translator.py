# Словник  (німецька - українська)
translation_dict = {
    "universität": "університет",
    "bibliothek": "бібліотека",
    "krankenhaus": "лікарня",
    "verkehrsmittel": "транспортний засіб",
    "lebensmittel": "продукти харчування",
    "naturwissenschaft": "природничі науки",
    "geschichte": "історія",
    "freundschaft": "дружба",
    "geschenk": "подарунок",
    "nachrichten": "новини",
    "ausstellung": "виставка",
    "arbeitsvertrag": "трудовий договір",
    "reisepass": "паспорт",
    "fremdsprache": "іноземна мова",
    "jahreszeit": "пора року"
}

# Введення слова для перекладу
word_to_translate = input("Введіть слово для перекладу (німецькою): ")
translation = translation_dict.get(word_to_translate.lower(), "Переклад не знайдено")
print(f"Переклад: {translation}")
