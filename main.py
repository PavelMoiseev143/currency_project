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


def list_currencies():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()

    for code, valute in data["Valute"].items():
        print(f"{code} - {valute['Name']}: {valute['Value']} руб.")


if __name__ == "__main__":
    while True:
        print("\n1 - Узнать курс валюты")
        print("2 - Конвертировать валюту в рубли")
        print("3 - Показать все валюты")
        print("0 - Выход")
        choice = input("Выберите действие (0,1,2 или 3): ")

        if choice == "1":
            currency = input("Введите код валюты (например, USD): ")
            get_currency_rate(currency)
        elif choice == "2":
            amount = float(input("Введите сумму: "))
            currency = input("Введите код валюты (например, USD): ")
            convert_to_rub(amount, currency)
        elif choice == "3":
            list_currencies()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")
