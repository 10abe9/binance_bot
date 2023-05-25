from binance.spot import Spot
import binance
import random

# Введите путь к файлу с api key, secret key
try:
    with open("C:\\Users\\qdaid\\Desktop\\bnnsspt.txt") as file:
        api_key, api_secret = file.read().split("\n")
except FileNotFoundError:
    api_key = input("Введите api key")
    api_secret = input("Введите secret key")


def test_api_file():
    assert api_key is not None
    assert api_secret is not None


inp = {
    "volume": 10000.0,  # Объем
    "number": 5,  # На сколько ордеров
    "amountDif": 50.0,  # Разброс
    "side": "SELL",  # Сторона торговли (SELL или BUY)
    "priceMin": 200.0,  # Нижний диапазон цены
    "priceMax": 300.0  # Верхний диапазон цены
}


def test_input(inp):
    assert inp["volume"] is not None
    assert inp["number"] is not None
    assert inp["amountDif"] is not None
    assert inp["side"] is not None
    assert inp["priceMin"] is not None
    assert inp["priceMax"] is not None


client = Spot(api_key, api_secret)
print(client.account())


def set_orders(volume: float, number: int, amountDif: float, side: str, priceMin: float, priceMax: float, ) -> bool:
    client = Spot(api_key, api_secret)
    params = {
        'symbol': 'BTCUSDT',
        'side': side,
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 0.002,
        'price': 1
    }
    for i in range(number - 1):
        order = random.randint(priceMin, priceMax)
        if volume < order:
            print(f"Всего удалось выполнить только {i} ордеров, больше денег нет ")
            return False
        else:
            volume -= order
        if side == "SELL":
            params["quantity"] = order
            response = client.new_order(**params)
            print(response)
        elif side == "BUY":
            params["quantity"] = order
            response = client.new_order(**params)
        else:
            volume += order
            print("Ваш ордер не может быть исполнен")
            return False
    order = random.randint(priceMin, priceMax)
    if volume > order:
        params["quantity"] = order
        response = client.new_order(**params)
        print(response)
    elif volume >= priceMin:
        params["quantity"] = order
        response = client.new_order(**params)
        print(response)
    else:
        print(f"Всего удалось выполнить только {number - 1} ордеров ")
        return False
    return True


try:
    set_orders(inp["volume"], inp["number"], inp["amountDif"], inp["side"], inp["priceMin"], inp["priceMax"])
except binance.error.ClientError:
    print("Вы неверно ввели свой ключ доступа.")
except ValueError:
    print("Пожалуйста, проверьте правильность введенных данных.")
