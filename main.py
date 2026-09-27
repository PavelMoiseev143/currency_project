from unittest import result
from urllib import response

import requests


def get_currency_rate(currency):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    valute = data["Valute"].get(currency)

    if valute:
        diff = valute["Value"] - valute["Previous"]
        arrow = "↑" if diff > 0 else "↓"
        percent = (diff / valute["Previous"]) * 100
        print(f"{valute['Name']}: {valute['Value']} руб. ({arrow} {diff:+.4f}, {percent:+.2f}%)")
    else:
        print("Такой валюты нет. Попробуйте ещё раз.")

def convert_to_rub(amount, currency):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    valute = data["Valute"].get(currency)

    if valute:
        result = amount * valute["Value"]
        print(f"{amount} {currency} = {result:.2f} руб.")
    else:
        print("Такой валюты нет. Попробуйте ещё раз.")

if __name__ == "__main__":
    print("1 - Узнать курс валюты")
    print("2 - Конвертировать валюту в рубли")
    choice = input("Выберите действие (1 или 2): ")

    if choice == "1":
        currency = input("Введите код валюты (например, USD): ")
        get_currency_rate(currency)
    elif choice == "2":
        amount = float(input("Введите сумму: "))
        currency = input("Введите код валюты (например, USD): ")
        convert_to_rub(amount, currency)
    else:
        print("Неверный выбор.")