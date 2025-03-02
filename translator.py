# Словник  (німецька - українська)
translation_dict = {
    "kraftfahrzeughaftpflichtversicherung": "страхування цивільної відповідальності автотранспортного засобу",
    "rindfleischetikettierungsüberwachungsaufgabenübertragungsgesetz": "закон про передачу обов’язків нагляду за маркуванням яловичини",
    "donaudampfschifffahrtsgesellschaftskapitän": "капітан Товариства пароплавства на Дунаї",
    "arbeitsunfähigkeitsbescheinigung": "довідка про непрацездатність",
    "rechtsschutzversicherungsgesellschaften": "страхові компанії правового захисту",
    "schifffahrtsgesellschaft": "судноплавне товариство",
    "siebentausendzweihundertvierundfünfzig": "сім тисяч двісті п’ятдесят чотири",
    "betäubungsmittelverschreibungsverordnung": "постанова про виписку наркотичних засобів",
    "sozialversicherungsfachangestellte": "співробітник соціального страхування",
    "unabhängigkeitserklärungen": "декларації незалежності",
    "straßenverkehrsordnung": "правила дорожнього руху",
    "versicherungsgesellschaft": "страхова компанія",
    "verkehrsüberwachungssystem": "система контролю дорожнього руху",
    "gebäudereinigungsunternehmen": "підприємство з прибирання будівель",
    "finanzdienstleistungsunternehmen": "фінансова сервісна компанія"
}

# Введення слова для перекладу
word_to_translate = input("Введіть слово для перекладу (німецькою): ")
translation = translation_dict.get(word_to_translate.lower(), "Переклад не знайдено")
print(f"Переклад: {translation}")