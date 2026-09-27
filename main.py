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

if __name__ == "__main__":
    currency = input("Введите код валюты (например, USD): ")
    get_currency_rate(currency)