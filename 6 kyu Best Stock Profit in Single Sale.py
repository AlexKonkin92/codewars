def max_profit(prices):  # способ через словарь, но дольше по производительности
    dict = {}
    for i in range(len(prices) - 1):
        key = prices[i]
        if key in dict and (max(prices[i + 1:]) - key) > dict[key]:
            dict[key] = max(prices[i + 1:]) - key
        elif key not in dict:
            dict[key] = max(prices[i + 1:]) - key
    return dict[max(dict, key=dict.get)]


def max_profit3(prices):  # через обновление переменной

    min_price = prices[0]
    max_profit = prices[1] - prices[0] if len(prices) > 1 else 0

    for price in prices[1:]:
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)
        min_price = min(min_price, price)

    return max_profit


if __name__ == "__main__":
    list_of_num = [10, 7, 5, 8, 11, 9]
    print(max_profit3(list_of_num))
