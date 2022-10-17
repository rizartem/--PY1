money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


# TODO Оформить решение


def lifetime(money_capital_, salary_, spend_, increase_):
    month_ = 0
    while (money_capital_) >= spend_:  # нужно проверять money_capital_ + salary_, если зп раньше расходов.
        money_capital_ = money_capital_ + salary_ - spend_
        spend_ = spend_ + spend_ * increase_
        month_ = month_ + 1
    return month_


life = lifetime(money_capital, salary, spend, increase)
print(life)
