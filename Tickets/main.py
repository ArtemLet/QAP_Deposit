amt = int(input('Введите колличество билетов: '))
age = [int(input(f'Введите возраст {i+1} посетителя: ')) for i in range(amt)]
price = 0
for v in age:
    if 18 <= v <= 25:
        price += 990
    elif v > 25:
        price += 1390
if len(age) > 3:
    price -= price * 0.1
print(f'Сумма к оплате: {int(price)} руб.')
