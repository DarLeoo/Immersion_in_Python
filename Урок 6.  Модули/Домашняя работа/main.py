from dir_1 import portfolio as pt


stock = {"AAPL": 1, "GOOGL": 5, "MSFT": 8}
price_initial = {"AAPL": 0.25, "GOOGL": 2500.75, "MSFT": 300.50}
price_current = {"AAPL": 13333.25, "GOOGL": 26300.75, "MSFT": 8030.50}


start_sum_value = pt.calculate_portfolio_value(stock, price_initial)
current_sum_value = pt.calculate_portfolio_value(stock, price_current)
print(f'Начальная стоимость портфеля акции: {pt.calculate_portfolio_value(stock, price_initial)}')
print(f'Текущаяя стоимость портфеля акции: {current_sum_value}')
profitability = pt.calculate_portfolio_return(start_sum_value, current_sum_value)
print(f'Доходность портфеля: {profitability} %')
max_value = pt.get_most_profitable_stock(stock, price_current)
print(f'Наиболее прибыльная акция: {max_value}')
