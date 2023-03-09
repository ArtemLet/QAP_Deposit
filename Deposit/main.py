money = int(input("Введите сумму которую планируете вложить под процент: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_list = list(map(float, per_cent.values()))
deposit = []
for per_el in per_list:
    d = money * per_el / 100
    deposit.append(d)
deposit = list(map(int, deposit))
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать — %d рублей" % max_deposit)
