per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("введите сумму\n"))
tkb = per_cent.get('ТКБ') * money / 100
skb = per_cent.get('СКБ') * money / 100
vtb = per_cent.get('ВТБ') * money / 100
sber = per_cent.get('СБЕР') * money / 100
deposit = [tkb, skb, vtb, sber]
deposit_max = max(deposit)
print(deposit)
print(deposit_max)
